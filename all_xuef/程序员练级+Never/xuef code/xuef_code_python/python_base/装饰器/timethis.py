""" python中的装饰器 """
from functools import wraps
import time

def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        # when func is called, log it
        print("[*] %s is called, args: %s" % (func.__name__, (*args, *kwargs)))
        end = time.time()
        return ret, "%.2fs" % (end-start) # !!!破坏了func的返回值协议
    return wrapper

@timethis # 等价于 add = timethis(add)
def add(*args):
    return sum(*args) # 不是重点，所以直接调用系统实现

print(add(range(1,101)))
