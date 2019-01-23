
"""
In python, objects are referenced by names. names are analogous to but not exactly
variables in C++ and Java.

>>> x = 5
In the above, example, x is a name that references the object, 5.
The process of assigning a reference to 5 to x is called binding.
A binding causes a name to be associated with an object in the innermost scope of
the currently executing program. Bindings may occur during a number of instances
such as during variable assignment or function or method call when the supplied parameter
is bound to the argument.

It is important to note that names are just symbols and they have no type
associated with them; names are just references to objects that actually have types.

"""
#names 无类型，它 ref的 object才有类型。
"""
x = 5
type(x) # 侦测的是 5的类型
"""

##Code Blocks
"""
Modules, functions and classes are all examples of code blocks.

A code block has a number of name-spaces associated with it.
"""

##namespace
"""
Namespaces
A namespace as the name implies is a context in which a given set of names is bound to objects.
Namespaces are implemented as dictionary mappings in python. The builtin namespace is an
example of a name-space that contains all the built-in functions and this can be accessed
by entering __builtins__.__dict__ at the terminal (the result is of a considerable amount).

The interpreter has access to multiple namespaces including the global name-space,
the builtin namespace and the local namespace.
These namespaces are created at different times and have different lifetimes.
For example, a new local namespace is created at the invocation of a function and
forgotten when the function exits or returns. The global namespace is created at
the start of the execution of a module and all names defined in this namespace
are available module wide while the built-in namespace comes into existence when
the interpreter is invoked and contains all the builtin names.
These three name-spaces are the main namespaces available to the interpreter.

"""

##Scopes
"""
A scope is an area of a program in which a set of name bindings (namespaces) is visible
and directly accessible without using any dot notation. At runtime, the following scopes
may be available.
·Inner most scope with local names
·The scope of enclosing functions if any (this is applicable for nested functions)
·The current module’s globals scope
·The scope containing the builtin namespace.
"""

###变量查找过程
"""
//ceval.c line2050
    case LOAD_NAME:
            w = GETITEM(names, oparg);
            if ((v = f->f_locals) == NULL) {
                PyErr_Format(PyExc_SystemError,
                             "no locals when loading %s",
                             PyObject_REPR(w));
                why = WHY_EXCEPTION;
                break;
            }
            if (PyDict_CheckExact(v)) {
                x = PyDict_GetItem(v, w);
                Py_XINCREF(x);
            }
            else {
                x = PyObject_GetItem(v, w);
                if (x == NULL && PyErr_Occurred()) {
                    if (!PyErr_ExceptionMatches(
                                    PyExc_KeyError))
                        break;
                    PyErr_Clear();
                }
            }
            if (x == NULL) {
                x = PyDict_GetItem(f->f_globals, w);
                if (x == NULL) {
                    x = PyDict_GetItem(f->f_builtins, w);
                    if (x == NULL) {
                        format_exc_check_arg(
                                    PyExc_NameError,
                                    NAME_ERROR_MSG, w);
                        break;
                    }
                }
                Py_INCREF(x);
            }
            PUSH(x);
            continue;

"""
###Lexical Scope
"""
Python supports static scoping also known as lexical scoping; this means that the visibility
of a set of name bindings can be inferred by only inspecting the program text.
"""

##Build symbol table
"""
The series of function calls run_mod -> PyAST_CompileObject -> PySymtable_BuildObject
triggers the process of building a symbol table.

"""














