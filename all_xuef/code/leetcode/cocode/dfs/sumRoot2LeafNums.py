"""
129. Sum Root to Leaf Numbers
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sumNumbers(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # 先序遍历(根-->左-->右)
    def preorder(node, rNodes, res):
        # 根(收集根?)
        rNodes.append(node.val)
        # 先序遍历左子树
        if node.left is not None:
            preorder(node.left, rNodes, res)
        # 先序遍历右子树
        if node.right is not None:
            preorder(node.right, rNodes, res)
        # 侦察叶子节点
        if node.left is None and node.right is None:
            print(rNodes)
            res.append(rNodes[:])
        rNodes.pop() # 删除列表中最后元素
    rNodes = []
    res = []
    preorder(root, rNodes, res)
    return [int("".join(map(str,s))) for s in res]
r = TreeNode(4)
n0 = TreeNode(0)
n9 = TreeNode(9)
n5 = TreeNode(5)
n1 = TreeNode(1)

r.left, r.right = n9, n0
n9.left, n9.right = n5, n1

rNodes = []
print(sumNumbers(r))



