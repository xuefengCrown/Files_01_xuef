"""
<SICP> p75
对树的映射

"""
t = [1, 2, [3, 4], 5, [6, 7]]

def scale_tree1(t: list):
    pass
# 实现scale_tree 的另一种方法是将树看作子树的序列，
# 并对它使用map
def scale_tree2(t: list, factor):
    def scale(subtree):
        if type(subtree) is list:
            # 这么神奇的麻
            return scale_tree2(subtree, factor)
        else:
            return subtree * factor
    return list(map(scale, t))

#print(scale_tree2(t, 10))

def square_tree(t: list):
    def square(subtree):
        if type(subtree) is list:
            return square_tree(subtree)
        else:
            return subtree * subtree
    return list(map(square, t))

#print(square_tree(t))


# 上面两个过程，大部分代码都是相似的。故可以做进一步抽象
# ???
def tree_map(proc, tree: list):
    def proc_subtree(subtree):
        if type(subtree) is list: # 如果子树仍是树，那么调用 tree_map 处理
            return tree_map(proc, subtree)
        else:
            return proc(subtree)

    return list(map(proc_subtree, tree))

def square_tree_with_tree_map(tree: list):
    def square(x):
        return x * x
    return tree_map(square, tree)

def scale_tree_with_tree_map(tree: list):
    def scale(x):
        return x * 20
    return tree_map(scale, tree)

print(square_tree_with_tree_map(t))
print(scale_tree_with_tree_map(t))






    

