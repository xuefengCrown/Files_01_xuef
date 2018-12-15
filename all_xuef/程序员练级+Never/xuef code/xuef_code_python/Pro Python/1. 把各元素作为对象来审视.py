
"""
Looking at things from a purely object-oriented perspective, it’s easy to understand how to work
with sequences that your code actually needs to use. You’ll have a concrete object, such as a list,
set or dictionary, which not only has data associated with it, but also has methods that allow for
accessing and modifying that data. You may need to iterate over it multiple times, access individual
items out of order or return it from the function for other code to use, all of which works well with
more traditional object usage.


The main benefit to this is memory allocation. A program designed to print out the entire range of
the Fibonacci sequence only needs to keep a few variables in memory at any given time, because each
value in the sequence can be calculated from the two previous values.

The main benefit to this is memory allocation. A program designed to print out the entire range of
the Fibonacci sequence only needs to keep a few variables in memory at any given time, because each
value in the sequence can be calculated from the two previous values. 


Python as a language offers a few different ways to iterate over a sequence without pushing all its
values into memory at once.

"""

# Python doesn’t take any measures to restrict access to that data.
"""
Python allows you to inspect a wide range of aspects of objects and the code that powers them.
In fact, you can even get access to the compiled bytecode that Python uses to execute functions.
Here are just a few examples of information available at runtime.
•  Attributes on an object
对象属性
•  The names of attributes available on an object
•  The type of an object
对象类型
•  The module where a class or function was defined
类或者函数所属模块
•  The filename where a module was loaded
模块加载自哪个文件
•  The bytecode for a given function
给定函数的字节码

Most of this information is only used internally, but it’s available because there are potential uses that
can’t be accounted for when code is first written. Retrieving that information at run-time is called
introspection内省 and is a common tactic in systems that implement principles like DRY.
"""












