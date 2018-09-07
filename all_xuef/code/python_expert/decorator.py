#coding:utf-8

"""
decorator
我能记得的几个例子：
1. time 函数的执行时间
2. 带记忆功能的函数

"""

"""
let's log it
"""
def logger(func_to_log):
    def wrapped(*args, **kwargs):
        print("Arguments are: %s, %s" % (args, kwargs))
        return func_to_log(*args, **kwargs) # call the real func

    return wrapped

def my_func(x, y):
    return x * y

print(my_func(10, 15))

my_logged_func = logger(my_func)
print(my_logged_func(10, 15))



