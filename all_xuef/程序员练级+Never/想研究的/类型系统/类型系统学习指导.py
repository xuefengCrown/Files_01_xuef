

#如果对后者有兴趣，那就学学Haskell喽。

"""
不知道题主目前的知识水平在什么位置，我就先假定你没有学过类型系统的任何知识但有
基本的函数式编程（functional programming）经验，所以先来说静态类型的类型推导，
然后再说动态类型语言。

首先，其实类型推导（Type Inference）只是一种延迟的类型检查（Type Checking）技术而已。
一般的编译原理书都把类型检查放在语义分析这部分来讲，这也就意味着你需要先做语法分析（Parsing）
来得到抽象语法树（AST）。当然如果你可以忍受Lisp 的语法，这步可以先省略。
其次，你最好要会写解释器，不用太复杂，只要给怎样写一个解释器 中的那个lambda 演算解释器加上
letrec 语义就可以开始下一步学习了（自己实现的时候一定要注意好好理解lookup 函数）。
学会了写解释器有很多好处：1. 直观地调试你的语言和类型系统，你肯定不希望你的类型系统只是个花架子吧；
2. 提前熟悉类型检查器的程序结构，你会发现类型检查和类型推导器的结构和普通解释器非常相似，
因为类型检查就是一种抽象解释；3. 还有一些好处下面说。


类型系统（Type System）最好的入门书当属《Types and Programming Languages》了。
这本书一开始从最简单的Untyped Lambda Calculus 开始先教你写解释器，但他的解释器用的是
Nameless Representation，这种解释器实现方式初看简单，但你会发现当你要给语言加特性、
扩展解释器的时候就必须要写一些很机械重复的代码而且还不好理解，所以我个人还是比较推荐
上面一段中的实现方式。然后跟着这本书重点学习并实现Simple Typed  Lambda Calculus 及其
扩展类型系统。在学完Subtyping 之后如果你觉得Recursive Types 难理解的话跳过它也无妨。
然后就是重头戏了：Polymorphism 和Type Inference。


有了实现Hindley-Milner System 的基础之后我建议继续深入阅读TAPL这本书剩下的部分，
虽然从System F 开始单纯的Type Inference 已经是Undecidable 的了，但更深入的类型系统学习
对现实中的编程语言还是很有必要学习的，比如你要做用户自定义类型就要学Type Operator (High-Order Types)、
再比如yinwang0/pysonar2 · GitHub 为Python推导出的类型是Intersection Type，而现今学界认为在为
动态类型语言做类型推导时Refinement Type 是更好的选择，而要理解Refinement Type 先搞定Dependent Type
再说。这部分有几篇论文我觉得是必读的：
《Practical Type Inference for Arbitrary-Rank Types》
《Advanced Topics in Types and Programming Languages》chapter 2
《A Tutorial Implementation of a Dependently Typed Lambda Calculus》
《Refinement Types for ML》


动态类型语言的类型推导目前是一个很前沿的问题，很多人在同时探索着不同的方法比如SpiderMonkey 用了
一种从运行时环境”反馈“信息以推进类型推导的方式，可以参考论文
《Fast and Precise Hybrid Type Inference for JavaScript》。
而Google 的V8 则是人工设定了很多rules 来帮助类型推导，这种方法我暂时没有找到论文。
同时，动态类型语言的类型推导一般是跟静态分析纠缠在一起的，这部分我也刚学，就只推荐两本书吧：
《Principles of Program Analysis》，《Data Flow Analysis: Theory and Practice》

最后，编程语言这个领域，论文、书籍上面的理论和实际语言的应用是有很大差距的，从Calculus 到Languages
往往有一道难以逾越的鸿沟，可以看看《Advanced Topics in Types and Programming Languages》chapter 10

https://www.zhihu.com/question/32473386/answer/55697951
"""


##
"""
@彭飞 已经很详细的介绍了如何“系统”地学习，我再介绍一下应该如何不系统的学习。
其实类型推导的基本概念是很简单的，但目前类型理论、程序分析理论等理论都用了太多的数学定义，
系统学习成本很高。非专业研究人员的话，我个人觉得不是特别必要。

类型推导的基本方法还是从程序中总结约束，然后求解约束的过程。动态语言和静态语言在这个过程上
并没有本质区别。而这里最关键的在于从哪些地方总结约束，但对于这个问题现在并没有通行理论可以学习，
所以只需要学总结约束->求解约束的大框架就行了。

我推荐看的是《Lecture notes on static analysis》中关于类型推导的一节，这一节在这本书的最前面，
很容易看懂。

作者：熊英飞
链接：https://www.zhihu.com/question/32473386/answer/92623423
"""
