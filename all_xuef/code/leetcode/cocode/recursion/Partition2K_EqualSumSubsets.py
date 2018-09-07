"""
698. Partition to K Equal Sum Subsets
Given an array of integers nums and a positive integer k, find whether
it's possible to divide this array into k non-empty subsets whose sums are all equal.
Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True

Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Note:
1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""

def canPartitionKSubsets(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    def canPart(nums, group_sums): # WRONG
        print(nums, group_sums)
        if nums == group_sums: return True
        
        g, n = group_sums[0], nums[0]
        if n > g: return False
        if n == g: return canPart(nums[1:], group_sums[1:])
        # [7, 5, 2, 2, 2, 2, 2] [15, 5, 2]
        # [5, 2, 2, 2, 2, 2]    [8, 5, 2]
        # [2, 2, 2, 2, 2]       [5, 3, 2]
        return canPart(nums[1:], sorted(group_sums[1:]+[g-n], reverse=True))
    def trans(nums, group_sums):
        print(nums, group_sums)
        if nums in group_sums: return True
        # [7, 5, 2, 2, 2, 2, 2] [[15, 5, 2]] # 7可以参与组合比它大的
        # [5, 2, 2, 2, 2, 2]    [[8, 5, 2]]
        # [2, 2, 2, 2, 2]    [[5, 3, 2], [8, 2]]
        n = nums[0]
        # 消化掉n后的所有可能组合情况
        tmp = [ele[:i] + ([ele[i]-n] if ele[i]>n else [])  + ele[i+1:] for ele in group_sums
                                             for i in range(len(ele)) if ele[i] >= n]
        #[[5, 3, 2], [8, 2]]
        group_sums = list(map(lambda x:sorted(x, reverse=True), tmp))
        # 消除group_sums中的重复元素
        group_sums_unique = []
        for i in group_sums:
            if i not in group_sums_unique:
                group_sums_unique.append(i)

        if nums[1:]: return trans(sorted(nums[1:], reverse=True), group_sums_unique)
        return False
    avg = sum(nums)//k if sum(nums)%k == 0 else -1
    if avg == -1: return False
    
    # [5, 4, 3, 3, 2, 2, 1], [5,5,5,5]
    return trans(sorted(nums, reverse=True), [[avg]*k])
nums, k = [4, 3, 2, 3, 5, 2, 1], 4
nums, k = [2,2,10,5,2,7,2,2,13], 3
nums, k = [2,2,2,2,3,4,5], 4

print(canPartitionKSubsets(nums, k))
