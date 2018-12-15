
"""
函数缓存允许我们将一个函数对于给定参数的返回值缓存起来。
当一个I/O密集的函数被频繁使用相同的参数调用的时候，函数缓存可以节约时间。
在Python 3.2版本以前我们只有写一个自定义的实现。
在Python 3.2以后版本，有个lru_cache的装饰器，允许我们将一个函数的返回值快速地缓存或取消缓存。

"""

# 我们来实现一个斐波那契计算器，并使用lru_cache。

from functools import lru_cache

@lru_cache(maxsize=32) # maxsize参数是告诉lru_cache，最多缓存最近多少个返回值。
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(60)])
