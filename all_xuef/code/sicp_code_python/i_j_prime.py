"""
Given N, find all (j, i, j+i) 0<j<i<=N, such that i+j is a prime
"""
N=6
enu_list = [(j, i, j+i) for i in range(1, N+1)\
            for j in range(1, i) if j<i]

#print(enu_list)

"""当然，这使用了语法糖，然而实际上发生了什么？
我们想尽可能去探知每个细节，这样才叫把握了它"""

def enum_interval(low, high):
    "生成low到high的整数序列，include high"
    return my_range(low, high+1)
def my_range(low, h):
    "如果你不想使用python的range()"
    if low == h:
        return []
    else:
        return [low]+my_range(low+1, h)
#print(enum_interval(1, 10))
def enum_pairs():
    def flatmap(map_list):
        fp = []
        for ele in map_list:
            fp = fp + ele
        return fp
    def span_i(i):
        def span_j(j):
            return (j, i, j+i)
        return list(map(span_j, enum_interval(1, i-1)))
    return flatmap(map(span_i, enum_interval(1, N)))

#fp = enum_pairs()
#print(fp)

def collect(pro, predicate, *args_list):
    









