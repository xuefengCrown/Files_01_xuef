
##在生成器 gen 中使用 yield from subgen()时，subgen 会获得控制权，
##把产出的值传给 gen 的调用方，即调用方可以直接控制 subgen。
##与此同时，gen 会阻塞，等待 subgen 终止。


#1. yield from 可用于简化 for 循环中的 yield 表达式。
def gen():
    for c in 'AB':
        yield c
    for i in range(1,3):
        yield i

p=print
##p(list(gen()))

def gen2():
    yield from 'AB'
    yield from range(1, 3)


#仅供教学使用。itertools 模块提供了优化版 chain 函数，使用 C 语言编写。
def my_chain(*iterables):
    for it in iterables:
        yield from it
s = 'ABC'
t = tuple(range(3))
##p(list(my_chain(s, t)))



#2. yield from 结构的本质作用无法通过简单的可迭代对象说明，而要发散思维，使用嵌套的生成器。
# yield from 是把职责委托给子生成器的句法

##yield from 的主要功能是打开双向通道，把最外层的调用方与最内层
##的子生成器连接起来，这样二者可以直接发送和产出值，还可以直接传
##入异常，而不用在位于中间的协程中添加大量处理异常的样板代码。有
##了这个结构，协程可以通过以前不可能的方式委托职责。

#委派生成器
##　　包含 yield from <iterable> 表达式的生成器函数。
#子生成器
##　　从 yield from 表达式中 <iterable> 部分获取的生成器。
#调用方
##　　PEP 380 使用“调用方”这个术语指代调用委派生成器的客户端代码。


























    
