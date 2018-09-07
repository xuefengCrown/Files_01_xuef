
"""

"""
# 这程序太他妈漂亮了，读起来就像读一篇短文;
def square_tree(tree):
    def handle_sub(sub_tree):
        def square(x):
            return x*x
        if type(sub_tree) is not list:
            return square(sub_tree)

        return square_tree(sub_tree)

    return list(map(handle_sub, tree))    

tree = [1,2,[3,4],[5,[6,7]]]
res = square_tree(tree)
print(res)
