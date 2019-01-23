
#0. 如何representing code???

#0.0 expression value && denoted value

#1. 如何能方便地添加 新类型和新操作?
##访问者模式
"""
麻烦在哪儿?
函数式中如何解决该问题? Java中为何不好处理?
因为 procedure 不是 first-class object???

Java 中可以在运行时根据对象类型来触发针对该对象的动作。所谓多态
这是一种行为的自动分发(基于对象类型)
This makes it easy to extend the table by adding new rows.
Simply define a new class.
这使得增加新类型很容易。
但是，增加列却很困难。
But imagine if you want to add a new operation—a new column.
In Java, that means cracking open each of those existing classes
and adding a method to it.

对于函数式语言: 添加 new op容易，但是添加新类型却困难。
Types and functions are totally distinct.
To implement an operation for a number of different types, you define a single function.
In the body of that you use pattern matching—sort of a type-based switch on steroids—
to implement the operation for each type all in one place.
This makes it trivial to add new operations—simply define another function that
pattern matches on all of the types.

But, conversely, adding a new type is hard. You have to go back and add a new case
to all of the pattern matches in all of the existing functions.


The Visitor pattern is really about approximating the functional style within an OOP language.
It lets us add new columns to that table easily. We can define all of the behavior for a new
operation on a set of types in one place, without having to touch the types themselves.
It does this the same way we solve almost every problem in computer science:
by adding a layer of indirection.

"""

#2. 优雅的错误报告

