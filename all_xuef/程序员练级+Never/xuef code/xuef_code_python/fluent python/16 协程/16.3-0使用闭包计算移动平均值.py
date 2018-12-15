
#定义一个高阶函数，用于生成一个闭包，在多次调用之间跟踪 total 和 count 变量的值。

def closure_averager():
    total = 0.0
    count = 0
    def avg(v):
        nonlocal count,total
        count += 1
        total += v
        return total/count
    return avg

p=print

averager = closure_averager()
for i in range(10):
    p(averager(i))
