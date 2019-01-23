# Object Lifetime and Storage Management
"""
In any discussion of names and bindings, it is important to distinguish between names
and the objects to which they refer.
names 只是访问object的入口(或者说便捷方式)

Creation of objects
Creation of bindings
Destruction of bindings
Destruction of objects

栈内存 vs 堆内存
Stack-Based Allocation
  Layout of run-time stack
Heap-Based Allocation

Garbage Collection

"""
# names and bingdings


# Scope Rules
"""
lexical scoping
dynamic scoping

"""


# procedure 之间如何沟通

# Module

# test Name Rules
"""
该语言静态还是动态作用域？作用域能够嵌套吗？开的还是闭的？
名字的作用域是延伸到它的声明所在的整个作用域，还是只包括声明之后？
怎样声明相互递归的类型或者子程序？
子程序可以作为参数传递吗，可以作为值返回吗，或者存入变量吗？
如果可以，其引用环境是何时约束的？

"""

# 探索
"""
3.26 Experiment with naming rules in your favorite programming language.
Read the manual, and write and compile some test programs. Does the
language use lexical or dynamic scope? Can scopes nest? Are they open or
closed? Does the scope of a name encompass the entire block in which it is
declared, or only the portion after the declaration? How does one declare
mutually recursive types or subroutines? Can subroutines be passed as parameters,
returned from functions, or stored in variables? If so, when are
referencing environments bound?

3.27 Listthekeywords(reservedwords)ofoneormoreprogramminglanguages.
List the predefined identifiers. (Recall that every keyword is a separate to-
ken. An identifier cannot have the same spelling as a keyword.) What cri-
teria do you think were used to decide which names should be keywords
and which should be predefined identifiers? Do you agree with the choices?
Why or why not?
"""



