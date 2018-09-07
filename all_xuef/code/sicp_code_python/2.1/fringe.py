"""
exer2.28
它以一个树(表示为表)为参数，返回一个表，表中元素是
这棵树的所有树叶，按照从左到右的顺序。
[[1,2],3]-->[1,2,3]
"""
# 是否以及如何用map实现？
def fringe(lst):
    if len(lst)==0: return []

    if type(lst[0]) is not list:
        return [lst[0]] + fringe(lst[1:])

    return fringe(lst[0]) + fringe(lst[1:])

lst=[3,4]
# if it works for [3,4]
# then it must work for [2,[3,4]]
lst=[2,[3,4]]
lst=[[1,2,[3,4]], [5,6]]
print(fringe(lst))

