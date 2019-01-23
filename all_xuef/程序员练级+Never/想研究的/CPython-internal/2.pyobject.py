
#PyObject: The core Python object
"""
Include/object.h
Objects/object.c
"""

##参考
"""
Python data model (Python API)
    https://docs.python.org/2/reference/datamodel.html
Python object protocol (C API)
    https://docs.python.org/2/c-api/object.html
"""

##target
"""
to be able to inspect any object in python and
understand the basis of its inner contents.
"""

##pythin data model
"""
Every piece of data is an object.
"""

##python -m dis test.py
##compile it to bytecode

##bytecode 讲解，参见 dis module
"""
LOAD_NAME    0(x)  ;;load value of x, and push it in value stack

STORE_NAME   1(y)  ;;pop thing off the stack, and assign it to y
"""


######################################################################
#how2inspect any object
"""
1. dir
  x=2
  dir(x)

  
"""
##java or c 中,int x=1; 只是allocate 4 bytes for it
##但是在 Python中,123 则是一个包装过的对象--PyObject, 它携带额外信息。
##这损失了一些性能,但是获得了一些 flexible
"""
1 + 2
-->num_val(1) + num_val(2)
-->num_val(int_add(1,2))
这不就是 plai 中所说的嘛!!!
"""

##__add__ 的意义
"""
假设你定义了 class Point
当你, p1 + p2, 实际上 Python解释器调用 Point类的 __add__方法
"""

##properties that all objects in python shares
"""
id(x)
type(x)
"""
###为什么我们可以 通过 id(1), type(1)来获得额外信息？
###这些信息存储在哪儿？
"""
所有的 对象都是一个 PyObject, 所以这些类型和id信息肯定是存在 PyObject 中!!!
"""

#because everything is an object, the operations are uniform!
"""
objects do not float around in memory; once allocated an object keeps
the same size and address.
Objects that must hold variable-size data can cintain pointers to variable-size
parts of the object.
Not all objects of the same type have the same size; but the size cann't change
after allocation.
(These restrictions are made so a reference to an object can be simply a pointer --
moving an object wolud require updating all the pointers, and changing an object's
zise would require moving it if there was another object right next to it.)
"""
######################################################################


#C source code
## PyObject
"""
typedef struct _object {
    Py_ssize_t ob_refcnt;
    struct _typeobject *ob_type;
} PyObject;


typedef struct {
    Py_ssize_t ob_refcnt;
    struct _typeobject *ob_type;
    long ob_ival;
} PyIntObject;
"""

##all objects can -->str
"""
every particular type implements its own version of it. (tp_str method)
这不就是 oop 的核心思想嘛?!
dynamic dispatching (根据对象的类型来分派到指定方法!)

generic add (BINARY_ADD)
"""
######################################################################























