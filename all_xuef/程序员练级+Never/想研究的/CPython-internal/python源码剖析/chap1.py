
#chap1
##在 PyTypeObject 中指定的不同的操作信息正是一种对象区别于另一种对象的关键所在。

##1.3 Python对象的多态性
"""
在 Python创建一个对象，比如PyIntObject 对象时，会分配内存，进行初始化，然后Python
内部会用一个 PyObject * 变量来保存和维护这个对象。
其他对象也与此类似，所以在 Python 内部各个函数之间传递的都是一种泛型指针--PyObject *
改制镇所指向的对象究竟是什么类型的，我们不知道，只能从指针所指对象的 ob_type 域动态进行判断，
而正是通过这个域， Python 实现了多态机制。

void Print(PyObject* object) {
  object->ob_type->tp_print(object);
}
"""

##1.4 引用计数(refcount)
"""
Python 内建了垃圾回收机制。
Python 通过对一个对象的引用计数的管理来维护对象在内存中的存在与否。
每个东西都是一个对象，都有一个 ob_refcnt 变量。
"""
##1.5 对象分类
"""
fundamental: type
Numeric: integer, float, boolean
Sequence: string, list, tuple
Mapping: dict
Internal: function,code,frame,module,method (运行时创建)
"""



























"""
