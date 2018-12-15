

#下述示例展示如何使用 iter 函数掷骰子，直到掷出 1 点为止：

from random import randint

def d6():
    return randint(1, 6)

d6_iter = iter(d6, 1)

#d6_iter #<callable_iterator object at 0x00000000029BE6A0>
for roll in d6_iter:
    print(roll)
