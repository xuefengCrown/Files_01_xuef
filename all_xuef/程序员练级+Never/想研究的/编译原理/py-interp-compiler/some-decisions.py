
#如何表示代码
#如何表示 value
"""
CodeBlock
  常量表constant table(java中的 常量池)
  符号表

The constant pool is an array of values. The instruction to load a constant
looks up the value by index in that array.

"""

#bytecode
"""
字节码占一个字节

字节码可能有参数

It’s kind of crazy to think that we can reduce all of the different AST classes
that we created in jlox down to an array of bytes and an array of constants.
There’s only one piece of data we’re missing.(符号表)

"""

#Line Information
"""
When a runtime error occurs, we show the user the line number of the offending source code.

In jlox, those numbers live in tokens, which we in turn store in the AST nodes.
We need a different solution for clox now that we’ve ditched syntax trees
in favor of bytecode.

Given any bytecode instruction, we need to be able to determine the line of the
user’s source program that it was compiled from.
Line information is only used when a runtime error occurs.
"""
##we have everything we need now to completely represent an executable piece of code
##at runtime in our virtual machine. 
"""
Remember that whole family of AST classes we defined in jlox?
In clox, we’ve reduced that down to three arrays:
bytes of code, constant values, and line information for debugging.

You can think of bytecode as a sort of compact serialization of the AST,
highly optimized for how the interpreter will deserialize it, in the order it needs.
In the next chapter, we will see how the virtual machine does exactly that.

"""
