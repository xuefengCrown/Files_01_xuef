
"""
(tree-sum '((1 2) (3 4)))

(1 2)，(1 (2 3)), ((1 2) 3) ((1 2) (3 4))

"""
def tree_sum(t):
    if is_leaf(t):
        return t
    else:
        return tree_sum(tree_left(t)) + tree_sum(tree_right(t))
    
#表达式谓词
def is_leaf(expr):
    return isinstance(expr, int)
def tree_left(t):
    return t[0]
def tree_right(t):
    return t[1]

def test_is_leaf():
    assert(is_leaf(1) == True)
    assert(is_leaf('a') == False)

def test_tree_sum():
    e1 = (1,2)
    e2 = ((1,2),(3,4))
    e3 = (1, (2, 3))
    e4 = ((1, 2), 3)
    assert(tree_sum( 1 ) == 1)
    assert(tree_sum( e1 ) == 3)
    assert(tree_sum( e2 ) == 10)
    assert(tree_sum( e3 ) == 6)
    assert(tree_sum( e4 ) == 6)
    
if __name__ == '__main__':
    test_is_leaf()
    test_tree_sum()
