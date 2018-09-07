
"""
scale_tree, square_tree-->tree_map
"""

def tree_map(proc, tree):
    def handle_sub(sub_tree):
        if type(sub_tree) is not list:
            return proc(sub_tree)
        return tree_map(proc, sub_tree)
    
    return list(map(handle_sub, tree))

def scale_tree(tree, factor):
    return tree_map(lambda x:x*factor, tree)

def square_tree(tree):
    return tree_map(lambda x:x*x, tree)

tree=[1,2,[3,4],[5,[6,7]]]
print(square_tree(tree))
print(scale_tree(tree, 10))
