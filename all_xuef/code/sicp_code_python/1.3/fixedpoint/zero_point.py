"""
折半法寻找函数f的零点
"""
import math
def search(f, neg_p, pos_p):
    """neg_p, pos_p对应的函数值为 - +
    """
    def average(x, y): return (x+y)/2.0
    def close_enough(x, y): return abs(x-y)<0.001
    mid_p = average(neg_p, pos_p)
    if close_enough(neg_p, pos_p): return mid_p
    else:
        test_value = f(mid_p)
        if test_value > 0:
            return search(f, neg_p, mid_p)
        elif test_value < 0:
            return search(f, mid_p, pos_p)
        else: return mid_p
        
def half_interval_method(f, a, b):
    a_v, b_v = f(a), f(b)
    if a_v<0 and b_v>0:
        return search(f, a, b)
    elif a_v>0 and b_v<0:
        return search(f, b, a)
    else:
        raise ValueError("values aren't of opposite sign")

m = half_interval_method(math.sin, 2.0, 4.0)
print(m)
