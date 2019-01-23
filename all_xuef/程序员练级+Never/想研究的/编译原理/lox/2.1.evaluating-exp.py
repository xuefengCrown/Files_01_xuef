
##编译到机器码
##转换到针对 VM 的字节码
##转换到另一 高级语言
"""
There are all manner of ways that language implementations make a computer do
what the user’s source code commands.

They can compile it to machine code, translate it to another high level language,
or translate to some bytecode format for a virtual machine that runs it.

For our first interpreter, though, we are going to take the simplest, shortest path
and execute the syntax tree itself.
"""

##QAQ
"""
1.What kinds of values do we produce?
2.How do we organize the code to execute expressions?
"""

##Representing Values
"""
Deep in the bowels of our interpreter are objects that represent Lox values.
They are created by literals, computed by expressions, and stored in variables.

To the user, they are Lox objects.
But to us, the language implementer, they are defined in terms of the
implementation language—Java in our case.
"""

##xuef
"""
value 是没有经过准确定义的！
3 是个值，但是它可以被解释为地址(loc,ref)
值存在哪儿? 栈上或者堆上，这些都要说清楚。
"""

##So how do we want to implement Lox values?
"""
Aside from the basic “pass around and store in variables”, we need to do a few things
with a given value:

1. Determine its type. Since Lox is dynamically typed, we need to be able to check the type
of a value at runtime to make sure you don’t do things like subtract a string from a number.

2. Tell if the object is truthy or not. When the object is used in something like an if condition,
we need to tell if that means the condition succeeds or not.

3. Tell if two objects are equal. We support == and != on all kinds of objects, so we need to be
able to implement that.
"""

##Here’s how we map each Lox type to Java:
"""
Lox type	Java representation
nil	            null
Boolean	            Boolean
number	            Double
string	            String
"""

##求值

###leaf nodes && atomic value
"""
literal: 字面量
variables
"""















