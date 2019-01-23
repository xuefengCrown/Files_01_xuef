
#python运行相关数据结构
"""
主要由PyCodeObject，PyFrameObject以及PyFunctionObject。
其中PyCodeObject是python字节码的存储结构
PyFrameObject是对栈帧的模拟，当进入到一个新的函数时，都会有PyFrameObject对象用于模拟栈帧操作。
PyFunctionObject则是函数对象，一个函数对应一个PyCodeObject,在执行def test():语句的时候会创建
PyFunctionObject对象。
而PyFrameObject和PyFunctionObject是动态结构，其中的内容会在运行时动态变化。

"""

##PyCodeObject对象
"""
python程序文件在执行前需要编译成PyCodeObject对象，每一个CodeBlock都会是一个PyCodeObject对象，
在Python中，类，函数，模块都是一个Code Block，也就是说编译后都有一个单独的PyCodeObject对象，
因此，一个python文件编译后可能会有多个PyCodeObject对象。
"""

##PyFrameObject对象
"""
python程序的字节码指令以及一些静态信息比如常量等都存储在PyCodeObject中，运行时显然不可能
只是操作PyCodeObject对象，因为有很多内容是运行时动态改变的。
"""
