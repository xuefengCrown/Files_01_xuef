
def f1():
    x = 1
    f2 = lambda y: x*y
    return f2

##x = 2
##f = f1()
##print(f(4)) # ==> 4

#静态作用域是指我们可以根据代码文本的位置，确定变量的存在区域。
"""
我猜你可能混淆了LEGB Rule和Dynamic Scoping，他们相同的地方都是由内向外逐层检查变量的定义是否存，
但是有闭包的lexical scoping是逐层向外检查Closure中变量是否存在，而dynamic scoping则是根据函数
调用链逐层向外检查变量是否存在，哪怕函数的定义不是嵌套的。

"""

#???
#闭包在Python里面的实现方式是保存一个通往外部namespace的指针(可以理解成一个dictionary)。


def foo():
    x = 1
    def inner(x=x): #参数的binding是在声明时发生的
        #inner函数的默认参数只会在函数生成的时候被引用一次，之后就会作为一个常量对象
        #被保存在inner函数里面，所以只会记下离它最近的那个x的值
        return x + 1 
    print(inner()) # output 2
    x = 2
    print(inner()) # output 2
#至于为什么么~就留给题主自己思考啦(Hint: Python的参数默认值的生成机制)。


def foo2():
    x = 1
    #Closures close over variables, not values. 
    def inner(): #inner定义时，关键是：捕获的是x的引用，而非值。
        return x + 1 
    print(inner()) # output 2
    x = 2
    print(inner()) # output 3

foo2()
