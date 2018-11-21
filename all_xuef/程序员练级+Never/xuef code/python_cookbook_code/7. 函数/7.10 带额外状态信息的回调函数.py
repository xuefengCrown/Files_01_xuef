
"""
问题
你的代码中需要依赖到回调函数的使用(比如事件处理器、等待后台任务完成后的回调等)，
并且你还需要让回调函数拥有额外的状态值，以便在它的内部使用到。
"""
##这一小节主要讨论的是那些出现在很多函数库和框架中的回调函数的使用——特别是跟异步处理有关的。
##为了演示与测试，我们先定义如下一个需要调用回调函数的函数：

# callback 前加*, 强制callback作为关键字参数传递
def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)

"""
实际上，这段代码可以做任何更高级的处理，包括线程、进程和定时器，但是这些都不是我们要关心的。
我们仅仅只需要关注回调函数的调用。下面是一个演示怎样使用上述代码的例子：
"""
def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

apply_async(add, (2, 3), callback=print_result)
#Got: 5
apply_async(add, ('hello', 'world'), callback=print_result)
#Got: helloworld

"""
为了让回调函数访问外部信息，一种方法是使用一个绑定方法来代替一个简单函数。
比如，下面这个类会保存一个内部序列号，每次接收到一个 result 的时候序列号加1：
"""
class ResultHandler:

    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))
#使用这个类的时候，你先创建一个类的实例，然后用它的 handler() 绑定方法来做为回调函数：
r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
#Got: 5
apply_async(add, ('hello', 'world'), callback=r.handler)
#Got: helloworld



#第二种方式，作为类的替代，可以使用一个闭包捕获状态值，例如：
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler
#下面是使用闭包方式的一个例子：
handler = make_handler()
apply_async(add, (2, 3), callback=handler)
#Got: 5
apply_async(add, ('hello', 'world'), callback=handler)
#Got: helloworld



##还有另外一个更高级的方法，可以使用协程来完成同样的事情：



"""
基于回调函数的软件通常都有可能变得非常复杂。一部分原因是回调函数通常会跟请求执行代码断开。
因此，请求执行和处理结果之间的执行环境实际上已经丢失了。如果你想让回调函数连续执行多步操作，
那你就必须去解决如何保存和恢复相关的状态信息了。

至少有两种主要方式来捕获和保存状态信息，你可以在一个对象实例(通过一个绑定方法)或者
在一个闭包中保存它。
"""

















