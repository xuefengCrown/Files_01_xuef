
"""
序列作为一种标准界面;

枚举器、过滤器、转换装置(映射，map)、累积器(accumulate, reduce)
"""
# enumerate map filter accumulate
# enumerate map filter reduce

import operator as ope
def null(seq):
    return len(seq) == 0
def accumulate(op, initial, seq):
    if null(seq): return initial
    return op(seq[0], accumulate(op, initial, seq[1:]))
    

def test():
    seq=list(range(11))
    res=accumulate(ope.add, 0, seq)
    print(res)

##test()
