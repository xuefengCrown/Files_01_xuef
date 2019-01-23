
#Python data types
"""
·Objects/abstract.c
·Include/stringobject.h
·Objects/stringobject.c
"""

##Learning Objective
"""
To understand how Python data types are "subtypes" of the core PyObject.
"""

##PyVarObject

##sequence types: list, tuple, string
"""
tuple is just an array of PyObject pointer.(对象指针数组)
"""
##all these assignments are just pointer assignment
##we do not copy objects, we copy pointers of objs
u=[1,2,3]
u[0] = "hello"

##C字符串, 只是有终结标识符的 character array

##Python string is immutable以及带来的好处
"""
1.just one copy for a string
2.
"""

##intern
"""
Java && Python 的string实现机制，都涉及这个词。
"""


##C source code 看字符串比较
"""
x = "hello"
y = "hello"
x == y

#bytecode COMPARE_TO
两个 PyObject*, 传递给generic compare函数。
每个类型都实现了自己的 compare 方法 (string_richcompare, 一个函数指针)
generic compare会侦测 PyObject的类型，然后调用该类型的特定 compare方法，
来实现比较。

richcmpfunc frich = RICHCOMPARE(v->ob_type);
if(frich != NULL){
  res = (*frich)(v, w, op);
}
"""
##Python 是动态类型语言，它会在runtime时侦测对象类型，然后根据其类型来分派方法。
##only at runtime we can exactly determine what to do! because compiler is stupid.
##defers all the decision at runtime (1 + "hello" 可编译通过，运行时出错)
"""
1 + 2
"hello" + "world"

都是 BINARY_ADD 指令
"""





























