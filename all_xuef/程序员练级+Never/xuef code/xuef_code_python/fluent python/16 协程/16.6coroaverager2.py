

#示例 16-13　coroaverager2.py：定义一个求平均值的协程，让它返回一个结果

from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None: #为了返回值，协程必须正常终止
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average) #Python 3.3 之前，如果生成器返回值，解释器会报句法错误。

"""
捕获 StopIteration 异常，获取 averager 返回的值
>>> coro_avg = averager()
>>> next(coro_avg)
>>> coro_avg.send(10)
>>> coro_avg.send(30)
>>> coro_avg.send(6.5)
>>> try:
... coro_avg.send(None)
... except StopIteration as exc:
... result = exc.value
...
>>> result
Result(count=3, average=15.5)
"""


"""
获取协程的返回值虽然要绕个圈子，但这是 PEP 380 定义的方式，当我
们意识到这一点之后就说得通了：yield from 结构会在内部自动捕获
StopIteration 异常。这种处理方式与 for 循环处理 StopIteration
异常的方式一样：循环机制使用用户易于理解的方式处理异常。对
yield from 结构来说，解释器不仅会捕获 StopIteration 异常，还
会把 value 属性的值变成 yield from 表达式的值。
"""
















