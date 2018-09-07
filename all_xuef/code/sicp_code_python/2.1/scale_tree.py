

"""
对树的映射

python 的变量名不能包含"-", 因为"-"会被解释为减操作;
"""
# [[1,2,3],[4,[5,6]]]
def scale_tree(tree, factor):
    def scale(sub_tree):
        if type(sub_tree) is not list:
            return sub_tree * factor
        else:
            return scale_tree(sub_tree, factor)
    
    return list(map(scale, tree))

tree, factor = [1,2,3], 10
tree = [[1,2,3],[4,[5,6]]]
##tree = []
res = scale_tree(tree, factor)
print(res)
