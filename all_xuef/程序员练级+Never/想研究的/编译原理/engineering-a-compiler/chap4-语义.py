#上下文相关分析

"""
须对输入程序的了解远超过语法这个层次。
对于输入程序中编码的计算过程的细节，编译器必须建立一个庞大的知识库。
编译器必须了解输入程序表示了哪些值、这些值驻留在何处、值是如何从一个名字流动到另一个名字的。
它必须理解计算过程本身的结构。必须分许程序与外部文件和设备的交互方式。

为基类进一步转换需要的上下文知识，编译器必须开发出一些方法，从语法之外的视角来考察程序。
它使用一些表示了代码某个方面的抽象，如类型系统、存储映射或控制流图。
编译器必须理解程序的命名空间：程序中表示的数据的种类、可以管道每个名字和表达式的数据的种类、
代码中出现的名字到改名字的特定实例的映射。
它必须理解控制流，无论是过程内还是过程间。

"""

#4.2 AN INTRODUCTION TO TYPE SYSTEMS
"""
Most programming languages associate a collection of properties with
each data value. We call this collection of properties the value’s type.

类型规定了属于该类型的所有值共有的一组性质。
"""

#4.2.1 The Purpose of Type Systems
"""
Programming-language designers introduce type systems so that they can
specify program behavior at a more precise level than is possible in a
context-free grammar.

类型系统建立了另一种词汇表来描述有效程序的形式和行为。
从类型系统的视角来分析一个程序所得到的信息是利用词法和语法分析无法得到的。
在编译器中，这种信息通常用于三种不同的目的：安全、表达力和运行时效率。
"""
##尽可能多地消除运行时错误
"""
未完成该目标，编译器首先必须为每个表达式推断出类型。
其次，编译器必须依照语言定义的规则，来检查每个运算符的操作数的类型。

Type inference
the process of determining a type for each name and each expression in the code.
"""
####隐式转换
"""
许多语言规定了规则，允许运算符使用不同类型的值，并要求编译器按需插入类型转换操作。
另一种备选方案是要求程序员指定显式转换。
"""
##安全性是使用强类型语言的一个重要原因。
"""
如果一种语言中每个表达式都能够分配一个无歧义的类型，这种语言称为强类型语言。
如果每个表达式都可以在编译时确定类型，我们称这种语言为静态类型的。
如果某些表达式只能在运行时确定类型，称这种语言为动态类型的。
"""
##提高表达力
"""
与上下文无关规则相比，具有良好结构的类型系统允许语言设计者更精确地规定程序的行为。
这种能力使得语言设计者可以加入一些上下文无关文法不可能表示的特性。
一个出色的例子就是运算符重载，即赋予运算符上下文相关的语义。

标准C语言使用函数原型，即函数参数数目和类型以及返回值类型的声明。
类型信息确定了C语言中指针递增的实际效果，地址实际增加的量由指针的类型决定。
面向对象语言使用类型信息为每个过程调用选择适当的实现。
"""

#类型检查
"""
程序员应该理解在给定的语言和编译器之下，类型检查是如何执行的。
"""

#4.2.2 类型系统的组件
"""
典型现代语言的类型系统有四个主要组件：
a set of base types, or built-in types;
rules for constructing new types from the existing types;
a method for determining if two types are equivalent or compatible;
rules for inferring the type of each source-language expression.

许多语言也包括了根据上下文将一种类型的值隐式转换为另一种类型的规则。
"""
##基础类型
"""
Lisp 的有理数，本质上是一对解释为比例的整数。
C语言没有字符串类型，因此C程序员代之以字符数组。
"""
####数字

####字符

####布尔值
"""
C语言将布尔值看作无符号整数的一个子区间，仅限于 0和 1。
"""

##Compound and Constructed Types
"""
Take, for example, Lisp, which provides extensive support for programming
with lists.Lisp’s list is a constructed type.

(cons first rest) 其中 first是一个对象，rest是一个列表实例。cons会创建一个列表。
Lisp 的实现可以检查对 cons的每个调用，以确认其第二个参数确实是一个列表实例。
"""
####1.数组
"""
使用最广泛的聚合对象之一。数组聚集了多个同一类型的对象，并赋予每个对象一个不同的名字。(隐式)
数组的基本性质是，程序可以使用数字下标来计算每个元素的名字。
一些语言在数组的类型信息中包含了其大小，因而 10x10 的整数数组与 12x12 的整数数组的类型是不同的。
大多数语言允许数组元素为任何基础类型，一些芋圆也允许使用构造类型作为数组元素。
"""
####2.串

####3.枚举类型
"""
Many languages allow the programmer to create a type that
contains a specific set of constant values.(包含常量值的特定集合)
"""
####4.结构和变体
"""
结构的类型是其各个成员类型的有序笛卡尔积。

经典观点将各个结构视作不同的类型。例如有两个子节点的树节点，其类型应当不同于有三个子节点的树节点。
从运行时系统的角度来看，将各种结构处理为不同的类型会导致整体途径复杂化。(为什么这么说?)
"""
####5.指针
"""
Pointers are abstract memory addresses that let the programmer manipulate
arbitrary data structures.
许多语言包含了指针类型。指针允许程序保存一个地址，而后考察位于该地址的对象。
创建对象的过程中也会创建指针(Java 中的 new, C 的 malloc)
一些语言提供了运算符来返回对象的地址，如C语言的 &

为防止程序员使用指向类型 t的指针引用类型 s的结构实例，一些语言限制对指针的赋值，
只能使用"等价"类型的地址。
在这些语言中，赋值运算符左侧的指针所指向的类型与右侧的表达式本身的类型必须是相同的。

Java’s new explicitly creates a typed object;
other languages use a polymorphic routine that takes the return type as a parameter.
"""
####多态性
"""
可以运作于不同类型参数之上的函数称为多态函数。
"""
##类型等价性
"""
对任何类型系统来说，都有一个关键组件，即用于判断两种不同类型声明是否等价的机制。
名字等价性 vs. 结构等价性(在表示类型时必须将类型本身的结构编码进来)
"""

##用于推断的规则
"""
操作数类型与结果类型之间的关系。
混合类型表达式可能是非法的。(如Java中，程序无法将数字赋值给字符)
一些语言要求编译器执行隐式类型转换。
"""
##声明和推断

##推断表达式的类型
"""
推断类型的目标是为程序中出现的每个表达式分配一个类型。
变量的类型、常数的类型、函数的类型。
"""
##类型推断的过程间相关问题
"""
函数调用。
编译器必须检查每个调用。实参类型兼容于形参。它还必须确定返回值的类型。

C语言中，通过函数原型来获得函数的类型信息。
Scheme中，函数 filter呈现出了所谓的参数化多态性。

为执行准确的类型推断，编译器需要每个函数的类型签名。
"""

#4.3 属性语法框架


































































































































































