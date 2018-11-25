"""
问题
你想在类中定义装饰器，并将其作用在其他函数或方法上。
"""
# 在类里面定义装饰器很简单，但是你首先要确认它的使用方式。比如到底是作为一个实例方法还是类方法。
from functools import wraps
class A:
    # decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("decorator 1")
            return func(*args, **kwargs)
        return wrapper
    # decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper

a=A()
@a.decorator1
def spam():
    print("spam..")
    pass
@A.decorator2
def grok():
    print("grok..")
    pass

spam()

















