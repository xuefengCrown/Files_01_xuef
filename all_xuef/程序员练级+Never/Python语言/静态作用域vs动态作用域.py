
##???
"""
Recall that Python uses Lexical Scoping, which controls what a newly created frame points to.
Lexical Scoping says: when calling a function, create a new frame that extends the environment
that the function was defined in.
Logo, however, uses a different rule -it uses Dynamic Scoping.
Dynamic Scoping says: when calling a function, create a new frame that extends the current frame.
"""

##为了实现 lexical scoping，我们必须把函数做成“闭包”（closure）。
##闭包是一种特殊的数据结构，它由两个元素组成：函数的定义和当前的环境。
"""
有意思的是，我们的解释器遇到 (lambda (x) e)，几乎没有做任何计算。
它只是把这个函数包装了一下，把它与当前的环境一起，打包放到一个数据结构（Closure）里面。
这个闭包结构，记录了我们在函数定义的位置“看得见”的那个环境。
稍候在调用的时候，我们就能从这个闭包的环境里面，得到函数体内的自由变量的值。
"""
