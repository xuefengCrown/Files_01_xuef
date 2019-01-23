

##assignment
"""
不管是Python还是C, 很重要的一个概念就是name 和 object。
在Python里面赋值语句有非常简洁的抽象概念，如下
  Assignment expression in Python have two things in common:
    Create a new object
    build a connection between that new object and a name
"""

##PyFrameObject
"""
我没有说PyFrameObject本身就是stack，因为PyFrameObject本身是为了隔离namespace而存在的。
而每一个PyFrameObject都有定义两个指针 -- PyObject **f_valuestack, PyObject ** f_stacktop
这两个指针模拟了x86平台里面的esp 和 ebp寄存器的作用。
"""

##
"""
PyEval_EvalFrameEx implements CPython’s evaluation loop, which is to say that it’s a function
that takes a frame object and iterates over each of the opcodes in its associated code object,
evaluating (interpreting, executing) each opcode within the context of the given frame
(this context is chiefly the associated namespaces and interpreter/thread states).
"""
