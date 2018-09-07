"""
exer2.35
将2.2.2节的count-leaves重新定义为一个累积
"""

import exer2_33 as funcs # 引入 _append
import accumulate as accu

# 枚举出树的所有叶子
def enumerate_tree(t): # [[1,2],3,4]-->[1,2,3,4]
    if len(t)==0: return []
    if type(t[0]) is not list:
        return funcs._append([t[0]], enumerate_tree(t[1:]))
    return funcs._append(enumerate_tree(t[0]), enumerate_tree(t[1:]))

# 使用map来定义 enumerate_tree???
def enumerate_tree_with_map(t):
    pass
    
# 将2.2.2节的count-leaves重新定义为一个累积
def count_leaves(tree):
    return accu.accumulate(lambda x,y:1+y,
                           0,
                           list(map(lambda x:1, enumerate_tree(tree))))
def test():
    t = [[1,2],3,4]
    print(enumerate_tree(t))
    print(count_leaves(t))
    
if __name__ == '__main__':
    test()
