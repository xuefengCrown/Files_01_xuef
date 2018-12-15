
# 官方doc: https://wiki.python.org/moin/Powerful%20Python%20One-Liners

# 1. 漂亮的打印
from pprint import pprint

my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
pprint(my_dict)


# 2. 列表辗平
## 使用itertools包中的itertools.chain.from_iterable轻松快速的辗平一个列表。

a_list = [[1, 2], [3, 4], [5, 6, [7, 8, 9, 'hello']]]
#print(list(itertools.chain.from_iterable(a_list)))
# Output: [1, 2, 3, 4, 5, 6]

# or
#print(list(itertools.chain(*a_list)))
# Output: [1, 2, 3, 4, 5, 6]

from collections import Iterable
def flatten(lst):
    for i in lst:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i
            
for i in flatten(a_list):
    print(i)

# 3. 一行式的构造器
## 避免类初始化时大量重复的赋值语句

class A(object):
    def __init__(self, a, b, c, d, e, f): # 要明白 __init__() 做了什么!!!
        print(locals())
        print(self.__dict__)
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})
        print(self.__dict__)

A(*range(6))





