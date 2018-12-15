
#coroaverager3.py：使用 yield from 计算平均值并输出统计报告

from collections import namedtuple
Result = namedtuple('Result', 'count average')

# 子生成器
def averager(): #1
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield #2main 函数中的客户代码发送的各个值绑定到这里的 term 变量上。
        if term is None: #3至关重要的终止条件。如果不这么做，使用 yield from 调用这个协程的生成器会永远阻塞。
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average) #4返回的 Result 会成为 grouper 函数中 yield from 表达式的值。

# 委派生成器
def grouper(results, key): #5
    while True: #6这个循环每次迭代时会新建一个 averager 实例
        #grouper 发送的每个值都会经由 yield from 处理，通过管道传给averager 实例。
        #grouper 会在 yield from 表达式处暂停，等待averager 实例处理客户端发来的值。
        #averager 实例运行完毕后，返回的值绑定到 results[key] 上。
        #while 循环会不断创建 averager 实例，处理更多的值。
        results[key] = yield from averager() #7
        #grouper 会在 yield from 表达式处暂停，等待averager 实例处理客户端发来的值。
        #而averager的运行和终止是由调用方来控制的!!!
        
# 客户端代码，即调用方
def main(data): #8这是驱动一切的函数。
    results = {}
    for key, values in data.items():
        #group 是调用 grouper 函数得到的生成器对象，传给 grouper 函数的第一个参数是 results，用于收集结果;
        #第二个参数是某个键。group 作为协程使用。
        group = grouper(results, key) #9
        next(group) #10预激 group 协程。
        for value in values:
            group.send(value) #11把各个 value 传给 grouper。传入的值最终到达 averager 函数中term = yield 那一行;
            #grouper 永远不知道传入的值是什么。
            
        group.send(None) # 重要 12把 None 传入 grouper，导致当前的 averager 实例终止，
        #也让grouper 继续运行，再创建一个 averager 实例，处理下一组值。
        
    # print(results) # 如果要调试，去掉注释
    report(results)

# 输出报告
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
                    result.count, group, result.average, unit))


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}
if __name__ == '__main__':
    main(data)

"""
这个试验想表明的关键一点是，如果子生成器不终止，委派
生成器会在 yield from 表达式处永远暂停。如果是这样，程序不
会向前执行，因为 yield from（与 yield 一样）把控制权转交给
客户代码（即，委派生成器的调用方）了。显然，肯定有任务无法
完成。

因为委派生成器相当于管道，所以可以把任意数量个委派生成器连接在一起：
一个委派生成器使用 yield from 调用一个子生成器，而那个子生成器本身也是委派生成器，
使用 yield from 调用另一个子生成器，以此类推。最终，这个链条要以一个只使用 yield
表达式的简单生成器结束;不过，也能以任何可迭代的对象结束。

任何 yield from 链条都必须由客户驱动，在最外层委派生成器上调用
next(...) 函数或 .send(...) 方法。可以隐式调用，例如使用 for循环。
"""

















































