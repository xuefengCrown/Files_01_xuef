
"""
问题
你想在函数上添加一个包装器，增加额外的操作处理(比如日志、计时等)。
"""

"""
装饰器涉及的知识比较多，要讲清楚，需要肢解
1. python中的额函数是对象，可以赋值给其他变量: new_print = print
2. 内嵌函数
3. 闭包
4. 无参数装饰器
5. 无返回值装饰器
6. 有参数，有返回值
7. 通用装饰器
8. python对装饰器的支持 @timethis
"""

import time
from functools import wraps

def timethis(func): # 这个函数名起的好
    """ Decorator that reports the execution time. """
    # @wraps(func) 注解是很重要的， 它能保留原始函数的元数据(下一小节会讲到)，
    # 新手经常会忽略这个细节。
    @wraps(func) # 可以不加, 加上有何作用?
    def wrapper(*args, **kwargs): # 使用 *args 和 **kwargs 来接受任意参数的函数
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, "executed time: %d s"%(end-start))
        return ret
    return wrapper # 这个新的函数包装器被作为结果返回来代替原始函数。


@timethis # ===> countdown = timethis(countdown)
def countdown(n):
    """ Counts down """
    while n > 0:
        n -= 1

countdown(10000000)
