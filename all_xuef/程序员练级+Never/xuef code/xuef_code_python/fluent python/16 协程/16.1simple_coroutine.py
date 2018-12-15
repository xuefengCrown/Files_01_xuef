


def simple_coroutine(): #
    print('-> coroutine started')
    x = yield # 
    print('-> coroutine received:', x)
    x = yield # 
    print('-> coroutine received:', x)
    
my_coro = simple_coroutine()
##首先要调用 next(...) 函数，因为生成器还没启动，没在 yield 语句处暂停，所以一开始无法发送数据。
next(my_coro) #预激

##调用这个方法后，协程定义体中的 yield 表达式会计算出 42;
##现在，协程会恢复，一直运行到下一个 yield 表达式，或者终止。
my_coro.send(42)
my_coro.send(100) 

def simple_coro2(a):
    print('-> Started: a =', a)

    #对于 b = yield a 这行代码来说，等到客户端代码再激活协程时才会设定 b 的值。
    #这种行为要花点时间才能习惯，不过一定要理解，这样才能弄懂异步编程中 yield 的作用（后文探讨）。
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)
