
"""
1. zip 用来干什么的
2. zip最佳实践
"""

import operator as op
opes = ['+', '-', '*', '/']
funcs = [op.add, op.sub, op.mul, op.truediv]

"""
Python2中直接返回一个由元组组成的列表;
Python3中返回的是一个对象，如果想要得到列表，可以用 list() 函数进行转换。
"""
d = zip(opes, funcs) # zip return a iterable object
print(list(d))
