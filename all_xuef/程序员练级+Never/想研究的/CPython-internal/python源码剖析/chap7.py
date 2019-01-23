
#Python 程序的执行过程
##虚拟机，字节码
"""
demo.py    Demo.java
demo.pyc   Demo.class
"""

##与 JVM相比，Python的虚拟机的抽象程度更高，距离真实机器更远。

##7.2 编译结果-->PyCodeObject 对象
"""
除了字节码之外，编译的结果中还包含其他一些信息，这些信息也是 Python执行程序时所必须的。

Python 对操作的便以结果就是字节码。那么对 字符串和常量值的处理结果是什么???

typedef struct {  
    PyObject_HEAD  
    int co_argcount;        // Code Block的参数的个数，比如说一个函数的参数  
    int co_nlocals;         // Code Block中局部变量的个数  
    int co_stacksize;       // 执行该段Code Block需要的栈空间  
    int co_flags;           // N/A  
    PyObject *co_code;      // Code Block编译所得的byte code，以PyStringObject的形式存在  
    PyObject *co_consts;    // PyTupleObject对象，保存Code Block中的常量  
    PyObject *co_names;     // PyTupleObject对象，保存Code Block中的所有符号  
    PyObject *co_varnames;  // Code Block中局部变量名集合  
    PyObject *co_freevars;  // 实现闭包所需东西  
    PyObject *co_cellvars;  // Code Block内部嵌套函数所引用的局部变量名集合  
    PyObject *co_filename;  // Code Block所对应的.py文件的完整路径  
    PyObject *co_name;      // Code Block的名字，通常是函数名或类名  
    int co_firstlineno;     // Code Block在对应的.py文件中的起始行  
    PyObject *co_lnotab;    // byte code与.py文件中source code行号的对应关系，以PyStringObject的形式存在  
    void *co_zombieframe;  
    PyObject *co_weakreflist;  
} PyCodeObject;  
"""
##对于代码中的一个 Code Block，会创建一个 PyCodeObject 对象与这段代码对应。
"""
怎样算一个 Code Block? Python的规则:
当进入一个新的名字空间，或者说作用域时，就算进入一个新的Code Block了。

[demo.py]
class A:
  pass
  
def fun():
  pass

a = A()
fun()

会创建 3个PyCodeObject 对象，一个是对应整个文件的，一个对应 class A， 一个对应 def fun。
"""
































