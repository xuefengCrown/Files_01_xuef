
##Python interpreter
"""
Python解释器是一个虚拟机,模拟真实计算机的软件。
我们这个虚拟机是栈机器，它用几个栈来完成操作
it manipulates several stacks to perform its operations
(与之相对的是寄存器机器，它从特定的内存地址读写数据)。

The Python interpreter is a bytecode interpreter: its input is instruction sets called bytecode.
When you write Python, the lexer, parser, and compiler generate code objects for the interpreter
to operate on. Each code object contains a set of instructions to be executed—that's the bytecode
—plus other information that the interpreter will need.

Bytecode is an intermediate representation of Python code: it expresses the source code that
you wrote in a way the interpreter can understand. It's analogous to the way that assembly
language serves as an intermediate representation between C code and a piece of hardware.

"""
