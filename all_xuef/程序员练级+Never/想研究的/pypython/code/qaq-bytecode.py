
#https://pyvideo.org/pycon-us-2012/stepping-through-cpython.html

#VM
"""
The python virtual machine is a stack based virtual machine so this means that
values for evaluations by an opcode are gotten from a stack and results of an
evaluation are placed back on the stack for further use by other opcodes.

"""

##QAQ
"""
·Where are the values such as that loaded by the LOAD_FAST instruction gotten from ?

·Where do arguments that are used as part of instructions come from ?

·How are nested function and method calls managed ? 4 How does the interpreter loop
handle exceptions ?

"""

##parsing
"""
·Parsing the python source code into a parse tree.
·Transforming the parse tree into an abstract syntax tree (AST).
·Generation of the symbol table.
·Generation of the code object from the AST. This step involves:
Transforming the AST into a flow control graph.
Emitting a code object from the control flow graph.


>>> import parser
>>> from pprint import pprint 
>>> st = parser.suite(code_str)
>>> pprint(parser.st2list(st))
"""
###Listing 3.3: The node data structure used in the python virtual machine
"""
1         typedef struct _node {
2             short		n_type;
3             char		*n_str;
4             int			n_lineno;
5             int			n_col_offset;
6             int			n_nchildren;
7             struct _node	*n_child;
8         } node;
"""

#3.3 From Parse Tree To Abstract Syntax Tree
"""
1         >>> import ast
2         >>> import pprint
3         >>> node = ast.parse(code_str, mode="exec")
4         >>> ast.dump(node)
5         ("Module(body=[FunctionDef(name='hello_world', args=arguments(args=[], "
6         'vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), '
7         "body=[Return(value=Str(s='hello world'))], decorator_list=[], "
8         'returns=None)])')

In the CPython implementation, the AST nodes are represented by C structures as
defined in the Include/Python-ast.h. 
"""

##3.4 Building The Symbol Table
"""
The symbol table just like the name suggest is a collection of the names within
a code block and the context in whic such names are used. The process of building
the symbol table involves the analysis of the names contained within a code block
and the assignment of the correct scoping to such names.

"""


##4. Python Objects
"""
When we say values are never declared as PyObjects but a pointer to any object
can be cast to a PyObject we are referring to an implementation detail dependent
on the C programming langugage and how it interprets data at memory locations.

1     typedef struct _object {
2         _PyObject_HEAD_EXTRA
3         Py_ssize_t ob_refcnt;
4         struct _typeobject *ob_type;
5     } PyObject;

The ob_refcnt field is used for memory management and the *ob_type is a pointer to a
type object that indicates the type of an object. It is this type that determines
what the data represents, what kind of data it contains and the kind of operations
that can be performed on that object.

Types in the VM are implemented using the _typeobject data structure defined in
the Objects/Object.h module. This is a C struct with fields for mostly functions
or collection of functions that are filled in by each type.

"""

##4.2 Under the cover of Types
"""
The _typeobject structure defined in Include/Object.h serves as the base structure of
all python types. The data structure defines a large number of fields that are mostly
pointers to C functions that implement some functionality for a given type.

1     typedef struct _typeobject {
 2         PyObject_VAR_HEAD
 3         const char *tp_name; /* For printing, in format "<module>.<name>" */
 4         Py_ssize_t tp_basicsize, tp_itemsize; /* For allocation */
 5 
 6         destructor tp_dealloc;
 7         printfunc tp_print;
 8         getattrfunc tp_getattr;
 9         setattrfunc tp_setattr;
10         PyAsyncMethods *tp_as_asyn; 
11 
12         reprfunc tp_repr;
13 
14         PyNumberMethods *tp_as_number;
15         PySequenceMethods *tp_as_sequence;
16         PyMappingMethods *tp_as_mapping;
17 
18         hashfunc tp_hash;
19         ternaryfunc tp_call;
20         reprfunc tp_str;
21         getattrofunc tp_getattro;
22         setattrofunc tp_setattro;
23 
24         PyBufferProcs *tp_as_buffer;
25         unsigned long tp_flags;
26         const char *tp_doc; /* Documentation string */
27 
28         traverseproc tp_traverse;
29 
30         inquiry tp_clear;
31         richcmpfunc tp_richcompare;
32         Py_ssize_t tp_weaklistoffset;
33 
34         getiterfunc tp_iter;
35         iternextfunc tp_iternext;
36 
37         struct PyMethodDef *tp_methods;
38         struct PyMemberDef *tp_members;
39         struct PyGetSetDef *tp_getset;
40         struct _typeobject *tp_base;
41         PyObject *tp_dict;
42         descrgetfunc tp_descr_get;
43         descrsetfunc tp_descr_set;
44         Py_ssize_t tp_dictoffset;
45         initproc tp_init;
46         allocfunc tp_alloc;
47         newfunc tp_new;
48         freefunc tp_free; 
49         inquiry tp_is_gc; 
50         PyObject *tp_bases;
51         PyObject *tp_mro;
52         PyObject *tp_cache;
53         PyObject *tp_subclasses;
54         PyObject *tp_weaklist;
55         destructor tp_del;
56 
57         unsigned int tp_version_tag;
58         destructor tp_finalize; 
59 } PyTypeObject;

The PyObject_VAR_HEAD field is an extension of the PyObject field that was discussed
in the previous section; this extension adds an ob_size field for objects that have
the notion of length.
A comprehensive description of each of the fields in this type object structure is
provided in the python C API documentation.

The important thing to note is that the fields in the strucutre each implement a part of
the type’s behaviour. Most of these fields are part of what we can call an object interface
or protocol because they map to functions in that can be called on python objects but
their actual implementation under the covers is type dependent.

For example, tp_hash field is a reference to a hash function for a given type - this field
can be left without a value in the case where instances of the type are not hashable;
whatever function is in the tp_hash field gets invoked when the hash method is called
on an instance of that type.


Also among these fields are fields for other python protocols such as the following.
1. Number protocol - A type implementing this protocol will have implementations for
PyNumberMethods *tp_as_number field. This field is a reference to a set of functions
that implement number like operations and it means that the type will support arithmetic
that have implementations included in the tp_as_number set. For example, the non-numeric
set type has an entry into this field because it supports arithmetic operations such
as -, <= and so on.

2. Sequence protocol - A type that implements this protocol will have a value in
the PySequenceMethods *tp_as_sequence field. This means that the type will support
some or all of the sequence operations such as len, in etc.

3. Mapping protocol - A type that implements this protocol will have a value in the
PyMappingMethods *tp_as_mapping. This will enable instance of such type to be treated
like python dictionaries using the dictionary subscripting syntax for setting and
accessing key-value mappings.

4. Iterator protocol - A type that implements this protocol will have a value in the
getiterfunc tp_iter and possibly the iternextfunc tp_iternext fields enabling instances
of the type to be used like python iterators.

5. Buffer protocol - A type implementing this protocol will have a value in the
PyBufferProcs *tp_as_buffer field. These functions will enable access to the instances
of the type as input/output buffers.

"""
##https://docs.python.org/3.6/c-api/typeobj.html


###4.3 Type Object Case Studies

####The type type???

####The object type???


##4.4 Minting type instances


###User-defined class
"""
1     class Test:
2         pass

The Test type as you would expect is an object of instance Type. To create an instance of
the Test type, the Test type is called as so - Test().

As always we can go down the rabbit hole to convince ourselves of what happens when the
type object is called.

type_call
This process provides an explanation for builtin types because afterall they have their
own tp_new and tp_init functions defined already but what about user defined types?
Most times, a user does not define a __new__ function for a new type (when defined this
will go into the tp_new field during class creation). The answer to this also lies with
the type_new function that fills the tp_new field of the Type. When creating a user defined
type such as in the case of Test, the type_new function checks for the presence of base
types (super types/classes) and when there are none, the PyBaseObject_Type type is added
as a default base type.

"""

####4.5 Objects and their attributes
"""
Types and their attributes (variables and methods) are central to object oriented programming.
Conventionally, types and instances store their attributes using a dict data structure -
this is not the full story in the case of instances when __slots__ are defined .
The dict data structure can be found in one of two places depending on the type of the object
as was mentioned in the previous section.

1. For objects that have a type of Type, the tp_dict slot of type structure is a pointer to
a dict that contains values, variables and methods for that type. In the more conventional
sense we say the tp_dict field of the type object data structure is a pointer to the type or
class dict.

2. For objects that have a type other than type (i.e instances of user defined types), that
dict data structure when present is located just after the PyObject structure that represents
the object. The tp_dictoffset value of the type of the object gives the offset from the start
of an object to this instance dict contains the instance attributes.

"""

####attributes finding
"""
the descriptor protocol - a protocol that is at the heart of attribute referencing in python.

Simply put, a descriptor is an object that implements the __get__, __set__ or __delete__
special methods of the descriptor protocol.
"""
####Listing 4.12: Algorithm for find a referenced attribute in an instance
####of a user defined type
"""
    1. type(b).__dict__ is searched for the attribute name. If the name is 
    found and it is a data descriptor, the result of calling the descriptor's
    __get__ method is returned. If the name is not found, then all base classes
    in the *mro* of type(b) are searched in the same way.
    2. b.__dict__ is searched and if attribute name is found here, it is 
    returned.
    3. if the name from 1 is a non-data descriptor the value of call
    __get__ is returned, 
    4. If the name is not found, an AttributeError is raised or __getattr__() 
    is called if provided by the user defined type. 

"""
##self
"""
A call such as b.name_balance_str() is actually the samething as type(b).name_balance_str(b).
The reason why we are able to invoke b.name_balance_str() is because the value returned by
b.name_balance_str is a method object which is a thin wrapper around the name_balance_str
with the instance already bound to the method instance. So when we make a call such as
b.name_balance_str() the method uses the bound instance as an argument to the wrapped
function hiding this detail from us.
"""














