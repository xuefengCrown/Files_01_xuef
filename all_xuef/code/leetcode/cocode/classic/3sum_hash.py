"""
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
    The solution set must not contain duplicate triplets.
Example:
    Given array nums = [-1, 0, 1, 2, -1, -4],
    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
关键问题：
1. nums 元素是否有重复
2. 输出是否有重复

分析：
要我们找出三个数且和为0，那么除了三个数全是0的情况之外，肯定会有负数和正数

我们对原数组进行排序，然后开始遍历排序后的数组，这里注意不是遍历到最后一个停止，
而是到倒数第三个就可以了。
这里我们可以先做个剪枝优化，就是当遍历到正数的时候就break，为啥呢，
因为我们的数组现在是有序的了，如果第一个要fix的数就是正数了，那么后面的数字就都是正数，就永远不会出现和为0的情况了。

"""
import collections as cll
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    tab = cll.defaultdict(list)
    for i in range(len(nums)):
        tab[nums[i]].append(i)
    #print(tab)
    # {-1: [0, 4], 0: [1], 1: [2], 2: [3], -4: [5]}
    sz = len(nums)
    # 所有数组下标对 i,j
    idx_pairs = [[i,j] for i in range(sz) for j in range(sz) if i != j]
    pairs = set()
    new_idx_pairs = []
    for i,j in idx_pairs:
        if not (nums[i],nums[j]) in pairs and not (nums[j],nums[i]) in pairs:
            pairs.add((nums[i],nums[j]))
            new_idx_pairs.append([i,j])
    rs = []
    for i,j in new_idx_pairs:
        sam = -nums[i]-nums[j]
        idxs = tab.get(sam)
        if not idxs: continue
        if idxs and len(set([i,j]+idxs)) >= 3:
            #print(sorted([nums[i], nums[j], sam]))
            if not sorted([nums[i], nums[j], sam]) in rs:
                rs.append(sorted([nums[i], nums[j], sam]))
    return rs
nums = [-1, 0, 1, 2, -1, -4]
#nums = [-7,-4,-6,6,4,-6,-9,-10,-7,5,3,-1,-5,8,-1,-2,-8,-1,5,-3,-5,4,2,-5,-4,4,7]
nums = [0,0,0]
print(len(threeSum(nums)))

#ans = [[-10,2,8],[-10,3,7],[-10,4,6],[-10,5,5],[-9,2,7],[-9,3,6],[-9,4,5],[-8,2,6],[-8,3,5],[-8,4,4],[-7,-1,8],[-7,2,5],[-7,3,4],[-6,-2,8],[-6,-1,7],[-6,2,4],[-5,-3,8],[-5,-2,7],[-5,-1,6],[-5,2,3],[-4,-4,8],[-4,-3,7],[-4,-2,6],[-4,-1,5],[-3,-2,5],[-3,-1,4],[-2,-1,3],[-1,-1,2]]
#my = [[-7,3,4],[-7,2,5],[-7,-1,8],[-4,-2,6],[-4,-1,5],[-4,-4,8],[-4,-3,7],[-6,-1,7],[-6,-2,8],[-6,2,4],[-10,4,6],[-9,3,6],[-5,-1,6],[-8,2,6],[-9,4,5],[-8,4,4],[-3,-1,4],[-9,2,7],[-10,5,5],[-10,3,7],[-10,2,8],[-8,3,5],[-2,-1,3],[-5,2,3],[-1,-1,2],[-5,-2,7],[-5,-3,8]]
##for i in my:
##    ans.remove(i)
##print(ans)
















