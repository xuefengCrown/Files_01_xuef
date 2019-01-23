
# 理解输入语言的语法和语义
"""
To translate text from one language to another, the tool must understand both
the form, or syntax, and content, or meaning, of the input language.

It needs to understand the rules that govern syntax and meaning in the output language.

Finally, it needs a scheme for mapping content from the source language to the target language.

"""

#The structure of a typical compiler
"""
The compiler has a front end to deal with the source language.
It has a back end to deal with the target language.
Connecting the front end and the back end, it has a formal structure for
representing the program in an intermediate form whose meaning is largely independent of
either language.
To improve the translation, a compiler often includes an optimizer that analyzes
and rewrites that intermediate form.
"""

#程序设计语言有着精确的性质和语义
"""
Computer programs are simply sequences of abstract operations written in
a programming language—a formal language designed for expressing computation.
Programming languages have rigid properties and meanings—as
opposed to natural languages.
"""
#目标语言通常是某种处理器的指令集

#Virtual machine
"""
A virtual machine is a simulator for some processor.It is an interpreter for
that machine's instruction set.
"""

#Interpreters and compilers have much in common.
"""
They perform many of the same tasks.
Both analyze the input program and determine whether or not it is a valid program.
Both build an internal model of the structure and meaning of the program.
Both determine where to store values during execution.
However, interpreting the code to produce a result is quite different from
emitting a translated program that can be executed to produce the result.
This book focuses on the problems that arise in building compilers.
However, an implementor of interpreters may find much of the material relevant.
"""

#why learn
##贪心算法(寄存器分配)
##启发式搜索技术(表调度)
##图算法(死代码消除)
##动态规划(指令选择)
##有限自动机和下推自动机(词法分析与语法分析)
##不动点算法(数据流分析)
"""
A good compiler contains a microcosm of computer science.
It makes practical use of greedy algorithms (register allocation),
heuristic search techniques (list scheduling),
graph algorithms (dead-code elimination), 
dynamic programming (instruction selection),
finite automata and push-down automata (scanning and parsing),
and fixed-point algorithms (data-flow analysis).
It deals with problems such as dynamic allocation,
synchronization,
naming,
locality,
memory hierarchy management,
and pipeline scheduling.
Few software systems bring together as many complex and diverse components.
Working inside a compiler provides practical experience in software
engineering that is hard to obtain with smaller, less intricate systems.
"""

#理论应用到实际
##自动产生词法分析器和语法分析器的工具应用了形式语言的成果
##这些工具也可用于文本搜索、网站过来、文字处理和命令行语言解释器
##类型检查和静态分析应用了格理论、数论和其他数学分支的结果，以理解和改进程序。
##代码生成器使用了树模式匹配、语法分析、动态规划和文本匹配的算法，来自动化指令选择的过程


##structure
"""
The front end focuses on understanding the source-language program.
The back end focuses on mapping programs to the target machine.
前端必须将其对源程序的认识编码到某种结构中，以供后端稍后使用。
中间表示(IR)成为了编译器对所转换代码的权威表示。
在一个两阶段编译器中，前端必须确保源程序是良构的，而且必须将输入的代码映射到 IR。
后端必须将IR 程序映射到目标机的指令集和有限的资源上。
由于后端仅处理前端生成的IR，因此它可以认为 IR不包括任何语法和语义错误。

The compiler can make multiple passes over the ir form of the code before
emitting(生成) the target program. This should lead to better code, as the compiler
can, in effect, study the code in one phase(阶段) and record relevant details. Then,
in later phases, it can use these recorded facts to improve the quality of
translation. This strategy requires that knowledge derived in the first pass be
recorded in the ir, where later passes can find and use it.
"""
#插入优化器
"""
优化器可以对 IR处理一遍或多遍，分析 IR并重写 IR。
"""

#front-end
##Checking Syntax
"""
To check the syntax of the input program, the compiler must compare the
program’s structure against a definition for the language.
This requires an appropriate formal definition, an efficient mechanism for testing
whether or not the input meets that definition.

Mathematically, the source language is a set, usually infinite, of strings
defined by some finite set of rules, called a grammar. Two separate passes
in the front end, called the scanner and the parser, determine whether or not
the input code is, in fact, a member of the set of valid programs defined by
the grammar.
数学上，元语言是一个字符串的集合，通常是无限集，由某种有限的规则集定义，后者称为语法。
"""

















