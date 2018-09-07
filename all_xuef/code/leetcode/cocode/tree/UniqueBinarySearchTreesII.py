"""
95. Unique Binary Search Trees II

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def generateTrees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    pass

def helper(nums): # (1,2,3,4)
    # 分解为规模更小的子问题
    # 写递归方法的难点在于如何适当的形式化问题,使得子问题
    # 与原问题具有某种一致性;
    # 注意什么叫一棵树,在命令式语言中我们可以用树根来表示一棵树
    # 因为如果我告诉你树根是什么,就等于把这棵树交给你了
    # 树根已经包含该树的全部信息
    # 相当于告诉你保险箱钥匙或密码
    """
    root为1,2,3,4的bst
    """
    if not nums: return [None]
    if len(nums)==1: return [TreeNode(nums[0])]
    roots = []
    # [[1, [], [2, 3]], [2, [1], [3]], [3, [1, 2], []]]
    rs=[[i,nums[:idx],nums[idx+1:]] for idx,i in enumerate(nums)]
    for circum in rs:
        root_val, l, r=circum
        ltrees,rtrees=helper(l), helper(r)
        for ltree in ltrees:
            for rtree in rtrees:
                root = TreeNode(root_val)
                root.left, root.right=ltree, rtree
                roots.append(root)
    
    print(rs)
    return roots
    
        
nums = [1,2,3]
helper(nums)

