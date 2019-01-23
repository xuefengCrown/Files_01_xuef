

"""
函数式语言基础
https://link.zhihu.com/?target=http%3A//lucacardelli.name/papers/typesystems.pdf
Basic Simple Type Theory

学学Haskell(先会用类型系统)
wikipedia


其次，你最好要会写解释器，不用太复杂，只要给怎样写一个解释器 中的那个lambda 演算解释器
加上letrec 语义就可以开始下一步学习了（自己实现的时候一定要注意好好理解lookup 函数）。

学会了写解释器有很多好处：
1. 直观地调试你的语言和类型系统
2. 提前熟悉类型检查器的程序结构，你会发现类型检查和类型推导器的结构和普通解释器非常相似，
因为类型检查就是一种抽象解释

类型系统（Type System）最好的入门书当属《Types and Programming Languages》了。

这本书一开始从最简单的Untyped Lambda Calculus 开始先教你写解释器，
但他的解释器用的是Nameless Representation，这种解释器实现方式初看简单，
但你会发现当你要给语言加特性、扩展解释器的时候就必须要写一些很机械重复的代码而且还不好理解，
所以我个人还是比较推荐上面一段中的实现方式。

然后跟着这本书重点学习并实现Simple Typed Lambda Calculus 及其扩展类型系统。

在学完Subtyping 之后如果你觉得Recursive Types 难理解的话跳过它也无妨。

然后就是重头戏了：Polymorphism 和Type Inference。


###############################
类型推导的基本方法还是从程序中总结约束，然后求解约束的过程。动态语言和静态语言在这个
过程上并没有本质区别。而这里最关键的在于从哪些地方总结约束，但对于这个问题现在并没有
通行理论可以学习，所以只需要学总结约束->求解约束的大框架就行了。
我推荐看的是《Lecture notes on static analysis》中关于类型推导的一节，
这一节在这本书的最前面，很容易看懂。



"""
