def rec_sum(nums):
    return nums[0]+rec_sum(nums[1:]) if nums else 0

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)

# 装饰器(trace函数调用次数)
def count_calls(f):
    ## 函数也是对象，可以有自己的属性
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

fib = count_calls(fib)
#rec_sum = count_calls(rec_sum)
fib(10)
p=print
p(fib.call_count)
