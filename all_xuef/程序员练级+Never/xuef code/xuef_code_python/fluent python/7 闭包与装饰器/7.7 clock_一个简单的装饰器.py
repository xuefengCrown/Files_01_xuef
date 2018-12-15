
# clockdeco2.py
import time
import functools
def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
            
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result
    return clocked

import functools

##除了优化递归算法之外，lru_cache 在从 Web 中获取信息的应用中也能发挥巨大作用。
@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__=='__main__':
    fibonacci(6)

"""
functools.lru_cache(maxsize=128, typed=False)
maxsize 参数指定存储多少个调用的结果。缓存满了之后，旧的结果会
被扔掉，腾出空间。为了得到最佳性能，maxsize 应该设为 2 的
幂。typed 参数如果设为 True，把不同参数类型得到的结果分开保
存，即把通常认为相等的浮点数和整数参数（如 1 和 1.0）区分开。顺
便说一下，因为 lru_cache 使用字典存储结果，而且键根据调用时传
入的定位参数和关键字参数创建，所以被 lru_cache 装饰的函数，它
的所有参数都必须是可散列的。
"""
    

