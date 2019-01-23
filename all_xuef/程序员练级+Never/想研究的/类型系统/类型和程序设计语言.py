# 前置知识
"""
有一定数学基础: 大学离散数学，算法和基础逻辑
至少熟悉一种函数式语言(如 Scheme, ML, Haskell)
程序语言和编译器的接班概念(抽象语法，BNF语法，求值，抽象机器等)
"""

#高级技术
"""
代数说明语言
模态逻辑
指称语义
Modern software engineering recognizes a broad range of formal methods for
helping ensure that a system behaves correctly with respect to some speci-
fication, implicit or explicit, of its desired behavior. On one end of the spec-
trum are powerful frameworks such as Hoare logic, algebraic specification
languages, modal logics, and denotational semantics.
"""

##函数类型
"""
we need to know what type the function returns.
Moreover, in order to be sure that the function will behave correctly when it is called,
we need to keep track of what type of arguments it expects.

为了讨论程序是否关于类型合法（即「良类型的」(well-typed) ），我们需要引入一套类型推理规则。
当使用这些规则推理一个表达式的类型时，我们称之为类型判断（type judgement）。
类型推理和判断使我们能推断lambda表达式的类型；
如果表达式的任一部分和类型判断结果不一致，则表达式非法。
（丘奇开始研究类型化LC的动机之一是区分「原子」值和「谓词」值，
他通过使用类型以确保谓词不能操作谓词，以试图避免的哥德尔式的悖论。）

我将采用一套不太正规的符号表示类型判断；标准符号太难用我目前使用的软件渲染了。
常用的符号跟分数有点像；分子由我们已知为真的语句组成；分母则是我们可以从分子中推断出来的东西。
我们经常在分子中使用一个叫「上下文」（context）的概念，它包含了一组我们已知为真的语句，
通常表示为一个大写的希腊字母。这里我用大写的希腊字母的名称表示。
如果一个类型上下文包含声明”x : A，我会写成 CONTEXT |- x : A。
对于分数形式的推理符号，我用两行表示，分子一行标有「Given: 」，分母一行标有「Infer: 」。
（正常符号用法可以访问维基百科的STLC页 。）
"""









