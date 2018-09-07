"""
114. Flatten Binary Tree to Linked List
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.pre = None
        def postorder(node):
            if not node: return None
            postorder(node.right)

            postorder(node.left)
            print(node.val)
            # ???
            node.right = self.pre
            node.left = None
            self.pre = node
               
        postorder(root)
root = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)

root.left, root.right = n2, n5
n2.left, n2.right = n3, n4
n5.right = n6

sol = Solution()
sol.flatten(root)

