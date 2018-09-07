# Definition for a binary tree node.
class TreeNode:
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None

from functools import reduce
import operator as op
def rightSideView(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    def nextLevelNodes(nodes):
        return list(filter(lambda x:x is not None,
                           reduce(op.add,list(map(lambda node:[node.left,node.right], nodes)))))
    def rightSideNode(nodes):
        if len(nodes)==0: return []
        print([n.val for n in nextLevelNodes(nodes)])
        return [nodes[-1].val] + rightSideNode(nextLevelNodes(nodes))
    if root is None: return []
    return rightSideNode([root])
    
r = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
##n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
r.left, r.right = n2,n3
n2.right = n5
n3.left = n6

print(rightSideView(r))
