"""
生成一个集合的所有子集

[1, 2, 3]
"""

def subsets(s):
    if len(s) == 0: return [[]]

    return subsets(s[1:]) + list(map(lambda x:([s[0]] + x), subsets(s[1:])))

s = [1, 2, 3]
print(subsets(s))
#print(list(map(lambda x:([2] + x), [[], [1]])))
