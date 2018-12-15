
# 缓存已经计算的值的函数

from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        nonlocal cache
        if args in cache:
            return cache[args]
        res = func(*args)
        cache[args] = res
        return res
    return wrapper

@memo
def fib(n):
    return 1 if n <= 2 else fib(n-1)+fib(n-2)

res = fib(45)
print(res)

