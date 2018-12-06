

##另一个常见的困惑是Python在闭包(或在周围全局作用域（surrounding global scope）)中 绑定变量的方式。

##您所写的
def create_multipliers():
    return [lambda x : i * x for i in range(5)]

##您所期望的
for multiplier in create_multipliers():
    print(multiplier(2))

##一个包含五个函数的列表，每个函数有它们自己的封闭变量 i 乘以它们的参数，得到:
##0
##2
##4
##6
##8
##
##而事实是
##8
##8
##8
##8
##8

##五个函数被创建了，它们全都用4乘以 x 。

##Python的闭包是 迟绑定 。 这意味着闭包中用到的变量的值，是在内部函数被调用时查询得到的。
##
##这里，不论 任何 返回的函数是如何被调用的， i 的值是调用时在周围作用域中查询到的。
##接着，循环完成， i 的值最终变成了4。

# it works
def create_multipliers():
    return [lambda x, i=i : i * x for i in range(5)]



