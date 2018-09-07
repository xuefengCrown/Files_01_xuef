"""
209. Minimum Size Subarray Sum
Given an array of n positive integers and a positive integer s, find the minimal
length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
你描述问题的方式，决定你的解法;
定义 ans(i)为以nums[i]开始的满足条件的最小子序列长度;
s = 7, nums = [2,3,1,2,4,3]
那么ans(0)=4 ([2,3,1,2])

这种重新描述和分解问题的方式，带来了 2 pointers 解法。
"""
def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    # 有几个特殊的case没有考虑到;
    if len(nums) == 0: return 0
    if sum(nums) < s: return 0
    if sum(nums) == s: return len(nums)
    # 也就是说, 我没有考虑过 下面代码能够得到正确结果的前置条件
    
    # assign a big number to ans
    ans = len(nums)+1
    left, sam = 0, 0
    for i in range(len(nums)):
        sam += nums[i]
        while sam >= s:
            # 找到了nums[left]开头, nums[i]结尾的满足条件的最短长度子列表
            # 此时left可以前进一步, 但是,i还不能往前走, ;
            # 因为以nums[i]结尾的满足条件的子列表可能还有
            print(left, "--", nums[left:i+1])
            # 尝试更新 ans
            ans = min(ans, i-left+1)
            sam -= nums[left]
            left += 1
            
    return ans
    
s, nums = 7, [2,3,1,2,4,3]
rs = minSubArrayLen(s, nums)
print("minSubArrayLen: ", rs)


