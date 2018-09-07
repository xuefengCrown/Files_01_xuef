"""
783. Minimum Distance Between BST Nodes
开始以为是父子节点之间; 原来是所有节点
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys
def minDiffInBST(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # 父子节点之间的差值
    def minDiff(node):
        # 太多条件判断, 我不喜欢目前这代码; 有更好的方法没?
        if node.left is None and node.right is None:
            return sys.maxsize
        if node.left is None:
            return min(node.right.val-node.val, minDiff(node.right))
        if node.right is None:
            return min(node.val-node.left.val, minDiff(node.left))

        return min(node.right.val-node.val, node.val-node.left.val, minDiff(node.left), minDiff(node.right))
    # 中序遍历, lst 收集节点
    def inorder(node, lst):
        if node.left is not None:
            inorder(node.left, lst)
        lst.append(node.val)
        if node.right is not None:
            inorder(node.right, lst)
    def minDiffBtwAll(node):
        lst = []
        inorder(root, lst)
        print(lst)
        # 寻找最小 diff
        minDiff = lst[1] - lst[0]
        for i in range(2, len(lst)):
            minDiff = min(minDiff, lst[i]-lst[i-1])
        return minDiff
    return minDiffBtwAll(root)
# sys.maxsize
r = TreeNode(4)
n2 = TreeNode(2)
n6 = TreeNode(6)
n1 = TreeNode(1)
n3 = TreeNode(3)

r.left, r.right = n2, n6
n2.left, n2.right = n1, n3
##r.left = n2
minDiffVal = minDiffInBST(r)
print(minDiffVal)







