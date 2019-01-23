
#Python--very dynamic language
"""
Full Python is a very dynamic language; one may insert new fields and methods into
classes or even into individual instances of classes at any time. One may redefine functions,
methods, modules, and classes at will.

标准python实现，同样是非常优秀的C源码项目。它利用中立的标准C语言，洗练的实现了动态面向对象环境，
使得Python语言的灵活和优雅得以充分体现。

Python的对象模型，以及它是如何映射到内存的。(通过 C)
"""

#Dynamic Typing: What the Compiler Doesn't Know
"""
One thing you've probably heard is that Python is a "dynamic" language—particularly that
it's "dynamically typed".

Python 是动态类型的，这意味着什么?

The Python compiler knows relatively little about the effect the bytecode will have.
It's up to the interpreter to determine the type of the object that BINARY_MODULO is
operating on and do the right thing for that type.
This is why Python is described as dynamically typed: you don't know the types of the
arguments to this function until you actually run it.

编译器的无知是优化Python的一个挑战 — 只看字节码，而不真正运行它，你就不知道每条字节码在干什么！
你可以定义一个类，实现__mod__方法，当你对这个类的实例使用%时，Python就会自动调用这个方法。
所以，BINARY_MODULO其实可以运行任何代码。

很难优化一个你不知道它会做什么的函数。在Russell Power和Alex Rubinsteyn的优秀论文中写道，
“我们可用多快的速度解释Python？”，他们说，“在普遍缺乏类型信息下，每条指令必须被看作一个
INVOKE_ARBITRARY_METHOD。”

"""
