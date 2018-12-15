

#coroaverager0.py：定义一个计算移动平均值的协程

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        #这里的 yield 表达式用于暂停执行协程，把结果发给调用方;
        #还用于接收调用方后面发给协程的值，恢复无限循环。
        term = yield average
        total += term
        count += 1
        average = total/count
"""
使用协程的好处是，total 和 count 声明为局部变量即可，
无需使用实例属性或闭包在多次调用之间保持上下文。
"""

#协程中未处理的异常会向上冒泡，传给 next 函数或 send 方法的调用方（即触发协程的对象）。

##示例 16-7 暗示了终止协程的一种方式：发送某个哨符值，让协程退
##出。内置的 None 和 Ellipsis 等常量经常用作哨符值。Ellipsis 的
##优点是，数据流中不太常有这个值。我还见过有人把 StopIteration
##类（类本身，而不是实例，也不抛出）作为哨符值；也就是说，是像这
##样使用的：my_coro.send(StopIteration)。

##从 Python 2.5 开始，客户代码可以在生成器对象上调用两个方法，显式地把异常发给协程。
##这两个方法是 throw 和 close。
