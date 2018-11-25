"""
你想在多个对象执行相同的操作，但是这些对象在不同的容器中，
你希望代码在不失可读性的情况下避免写重复的循环。
"""

#itertools.chain() 方法可以用来简化这个任务。

nums=[1,2,3,4,5]
cs=['x', 'y', 'z']
from itertools import chain
for x in chain(nums, cs):
    print(x, end=' ')
