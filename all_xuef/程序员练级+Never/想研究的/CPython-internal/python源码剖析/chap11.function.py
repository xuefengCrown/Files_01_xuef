
#在 Python中，任何东西都是一个对象，函数也不例外。
##PyFunctionObject对象的定义如下：
"""
typedef struct {
    PyObject_HEAD
    PyObject *func_code;    /* A code object */
    PyObject *func_globals; /* A dictionary (other mappings won't do) */
    PyObject *func_defaults;    /* NULL or a tuple */
    PyObject *func_closure; /* NULL or a tuple of cell objects */
    PyObject *func_doc;     /* The __doc__ attribute, can be anything */
    PyObject *func_name;    /* The __name__ attribute, a string object */
    PyObject *func_dict;    /* The __dict__ attribute, a dict or NULL */
    PyObject *func_weakreflist; /* List of weak references */
    PyObject *func_module;  /* The __module__ attribute, can be anything */
} PyFunctionObject;
"""

## PyCodeObject 与 PyFunctionObject
"""
PyCodeObject是对一段 Python 源代码的静态表示。
一个 Code Block 会产生一个且只有一个 PyCodeObject，这个 PyCodeObject 对象
中包含了这个 Code Block 的一些静态的信息，所谓静态的信息是指可以从源代码中看到的信息。
这些信息会被存储在 PyCodeObject的常量表 co_consts, 符号表 co_names 以及字节码序列 co_code 中。

而 PyFunctionObject则不同，该对象是 Python代码在运行时动态产生的，更准确地说，是在执行一个 def
语句的时候创建的。在 PyFunctionObject中，当然会包括这个函数的静态信息，这些信息存储在 func_code
中，实际上， func_code 一定会指向函数代码对应的 PyCodeObject 对象。
除此之外， PyFunctionObject对象中还包含了一些函数在执行时必须的动态信息，即上下文信息，
比如 func_globals, 就是函数在执行时关联的 global作用域。
global 作用域中的符号和值的对应关系必须在运行时才能确定，所以这部分必须在运行时动态创建。

"""

##11.3 函数执行时的名字空间
"""
在执行 func_0.py 的字节码指令序列时的 global名字空间和执行函数 f 的字节码指令序列时的
global 名字空间实际上是同一个名字空间。
"""

























