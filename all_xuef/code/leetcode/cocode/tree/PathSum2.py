"""
113. Path Sum II
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # sum函数被局部变量覆盖，所以自己定义一个
        def mysum(lst):
            if len(lst) == 0: return 0
            return lst[0] + mysum(lst[1:])
        self.roots = [] # 收集path根节点
        self.res = []
        # 先序遍历
        def preorder(node):
            if not node: return
            self.roots.append(node.val)
            preorder(node.left)
            preorder(node.right)
            # 遇到根节点
            if not node.left and not node.right:
                #print(self.roots)
                if mysum(self.roots) == sum:
                    self.res.append(self.roots[:])
            self.roots.pop()

        if not root: return []   
        preorder(root)
        return self.res
# 构造一棵树
a5 = TreeNode(5)
b4 = TreeNode(4)
c8 = TreeNode(8)
d11 = TreeNode(11)
e13 = TreeNode(13)
f4 = TreeNode(4)
g7 = TreeNode(7)
h2 = TreeNode(2)
i5 = TreeNode(5)
j1 = TreeNode(1)

a5.left, a5.right = b4, c8
b4.left = d11
c8.left, c8.right = e13, f4
d11.left, d11.right = g7, h2
f4.left, f4.right = i5, j1

sol = Solution()
sol.pathSum(a5, 22)
