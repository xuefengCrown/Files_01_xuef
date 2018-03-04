"""
处理层次性结构
((1, 2), 3, 4)
"""

t = (1, 2)
hs = ((1, 2), 3, 4, (5, (6, (7, 8))))
#print(type(1))
#print(len(hs))

def count_leaves(t: tuple):
    if len(t) == 0: return 0
    if type(t[0]) is tuple:
        return count_leaves(t[0]) + count_leaves(t[1:])
    else:
        return 1 + count_leaves(t[1:])

def deep_reverse(t: list):
    if len(t) == 0: return []
    if type(t[0]) is list:
        return deep_reverse(t[1:]) + [deep_reverse(t[0])]
    else:
        return deep_reverse(t[1:]) + [t[0]]

def fringe(t: list):
    if len(t) == 0: return []
    if type(t[0]) is list:
        return fringe(t[0]) + fringe(t[1:])
    else:
        return [t[0]] + fringe(t[1:])
print(count_leaves(hs))
t1 = [1, 2, [3, 4]]
print(deep_reverse(t1))
print(fringe(t1))
