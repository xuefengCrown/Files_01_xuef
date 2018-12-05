
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)

def f(n):# 1 2 4 8 16
    if n == 1:
        return 1
    if n == 2:
        return 2
    return 2*f(n-2) + f(n-1)

def memo(f):
    cache = {} # 1. {}是mutable object, 所以不需要nonlocal声明
    #The use of a dictionary requires that the argument to the memoized function be immutable.
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

# 2. 每次调用memo,都会有一个新的cache
fib = memo(fib)
f = memo(f)
print(f(5))
print(fib(5)) # 5

