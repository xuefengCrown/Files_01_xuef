"""问题: 你想定义一个可以接受参数的装饰器"""
# 假设你想写一个装饰器，给函数添加日志功能，同时允许用户指定日志的级别和其他的选项。
from functools import wraps
import logging
def logged(level, name=None, msg=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    def decorate(func):
        logname = name if name else func.__name__
        log = logging.getLogger(logname)
        logmsg = msg if msg else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

@logged(logging.DEBUG)# ===> add = logged(logging.DEBUG)(add)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

# @decorator(x, y, z) 等价于 func = decorator(x, y, z)(func)
# def func(): pass















        
