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
因为我们的数组现在是有序的了，如果第一个要fix的数就是正数了，那么后面的数字就都是正数，
就永远不会出现和为0的情况了。
"""
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def seek_match(sam, nums): # 为sam寻找匹配的数对
        rs = []
        i, j = 0, len(nums)-1
        while j > i:
            if nums[j]+nums[i] == sam:
               rs.append([-sam, nums[j], nums[i]])
               while (i < j and nums[i] == nums[i + 1]): i += 1
               while (i < j and nums[j] == nums[j - 1]): j -= 1
               i += 1
               j -= 1
            elif nums[j]+nums[i] < sam: i += 1
            else: j -= 1
        return rs

    nums.sort()
    sz, rs = len(nums), []
    for idx,k in enumerate(nums[:-2]):
        if k > 0: break
        if (idx > 0 and nums[idx] == nums[idx-1]): continue
        
        i, j = idx+1, sz-1
        while j > i:
            s = nums[j]+nums[i] + k # 不要有任何重复计算
            if s == 0:
               rs.append([k, nums[j], nums[i]])
               while (i < j and nums[i] == nums[i + 1]): i += 1
               while (i < j and nums[j] == nums[j - 1]): j -= 1
               i += 1
               j -= 1
            elif s < 0: i += 1
            else: j -= 1
    return rs
##    uniques = []
##    for i in rs: # 消除重复
##        if not i in uniques: uniques.append(i)
##    return uniques
        
nums = [-1, 0, 1, 2, -1, -4]
nums = [-7,-4,-6,6,4,-6,-9,-10,-7,5,3,-1,-5,8,-1,-2,-8,-1,5,-3,-5,4,2,-5,-4,4,7]
#nums = [0,0,0]
print(threeSum(nums))














