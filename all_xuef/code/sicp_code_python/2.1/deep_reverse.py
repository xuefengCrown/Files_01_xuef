
"""
exer2.27
"""
def reverse_list(lst):
    if len(lst)==0: return []
    return [lst[-1]] + reverse_list(lst[:-1])

# 是否以及如何用map实现？
# [[1,2], [3,4]]
# 如何形式化证明，我的递归是正确的？
def deep_reverse(lst):
    if len(lst)==0: return []

    if type(lst[-1]) is not list:
        return [lst[-1]] + deep_reverse(lst[:-1])

    return [deep_reverse(lst[-1])] + deep_reverse(lst[:-1])

lst = [[1,2],[3,[4,5,6]]]
##lst = [1,2]
print(deep_reverse(lst))

# test
lst = [1,2]
lst = [[3,4]]

