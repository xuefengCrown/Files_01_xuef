#类型系统开篇
"""
类型（type），是编程语言中一个经常被人们提及的概念，
当我们看待一门编程语言的时候，言必谈之类型系统（type system）。

它
是显式类型的（explicit typing），还是隐式类型的（implicit typing），
是静态类型的（static typing），还是动态类型的（dynamic typing），
其类型检查（type check）是较强的（stronger），还是较弱的（weaker）。

它
是否支持高阶类型（high-order type），
是否支持递归类型（recusive type），
是否支持子类型（subtype），
是否支持多态（polymorphism）。

"""

##然而，我发现理解它们并不容易，我们欠缺最基本的数理逻辑和证明论相关的知识。
"""
类型系统，可以看做是附着在语言语法之上的一套符号证明系统。
In programming languages, a type system is a set of rules that
assigns a property called type to the various constructs of a computer program,
such as variables, expressions, functions or modules.
"""

##前置知识
"""
给表达式确定类型的过程，相当于对程序应该具备的属性做形式证明，
因此，数理逻辑是我们的朋友。

另一方面，从语义（semantics）角度对类型进行理解，我们会遇到更大的阻碍，
因为，这又涉及到了公理集合论和代数学相关的必备知识。

本系列文章，
我计划从无类型 \lambda 演算开始，逐步介绍简单类型（simply typed） \lambda 演算，
介绍递归类型和不动点（fixed point）之间关系，介绍组合子逻辑（combinatory logic）。

然后，回归到本原，学习命题逻辑和一阶谓词逻辑相关的内容，
建立起逻辑学与类型理论之间的桥梁。

时间允许的话，我们还可以探讨模型论相关的内容，在补充了代数学相关的内容之后，
我们就可以讨论CPO，Henkin模型，Kripke模型，以及笛卡儿闭范畴（CCC）了。

"""



