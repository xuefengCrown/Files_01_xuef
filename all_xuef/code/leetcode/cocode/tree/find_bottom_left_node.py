 #Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findBottomLeftValue(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # 中序遍历二叉树
    def inorder(node, deepth):
        if node.left is not None:
            deepth[0] += 1 # 更新向左探索的深度
            inorder(node.left, deepth)

        print("visit:", deepth[0], node.val)
        if deepth[0] >= deepth[2]: 
            deepth[1] = node.val
            deepth[2] = deepth[0]
            print(deepth)
             
        if node.right is not None:
            inorder(node.right, deepth)
            
        deepth[0] -= 1 
        
    deepth = [1, 0, 1]
    inorder(root, deepth)
    return deepth[1]
    
##r = TreeNode(1)
##n2 = TreeNode(2)
##n3 = TreeNode(3)
##n4 = TreeNode(4)
##n5 = TreeNode(5)
##n6 = TreeNode(6)
##n7 = TreeNode(7)
##n8 = TreeNode(8)
##
##r.left, r.right = n2, n3
##n2.left = n4
##n3.left, n3.right = n5, n6
##n4.right = n7
##n7.left = n8

# [2,1,3]
r = TreeNode(2)
n1 = TreeNode(1)
n3 = TreeNode(3)

r.left, r.right = n1, n3
rs = findBottomLeftValue(r)
print(rs)
