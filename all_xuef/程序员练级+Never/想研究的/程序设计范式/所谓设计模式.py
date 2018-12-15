
# http://www.yinwang.org/blog-cn/2013/03/07/design-patterns

##所谓的 visitor，本质上就是函数式语言里的含有“模式匹配”（pattern matching）的递归函数。
##在函数式语言里，这是多么轻松的事情。
##可是因为 Java 没有模式匹配，所以很多需要类似功能的人就得使用 visitor pattern。

##为了所谓的“通用性”，他们往往把 visitor pattern 搞出多层继承关系，
##让你转几道弯也搞不清楚到底哪个 visitor 才是干实事的。
