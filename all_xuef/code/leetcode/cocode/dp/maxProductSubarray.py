"""
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.
Example 1:
    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
"""

"""
状态：
    记dp_max[i]为 以nums[i]开头的积最大子串
    记dp_min[i]为 以nums[i]开头的积最小子串
    dp[i]-->dp[i-1]
方程：
    dp_max[i] = max(dp_max[i+1] * nums[i], dp_min[i+1] * nums[i], nums[i])
    dp_min[i] = min(dp_max[i+1] * nums[i], dp_min[i+1] * nums[i], nums[i])
    将转移方程与函数类比; dp_max[i] = f(x, y, z, ...)
初始化：
    ...
结果：

"""
def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1: return nums[0]

    dp_max = nums[:]
    dp_min = nums[:]
    for i in reversed(range(len(nums)-1)):
        dp_max[i] = max(dp_max[i+1] * nums[i], dp_min[i+1] * nums[i], nums[i])
        dp_min[i] = min(dp_max[i+1] * nums[i], dp_min[i+1] * nums[i], nums[i])
    
    print("nums ", nums)
    print("dp_max ", dp_max)
    print("dp_min", dp_min)
    return max(dp_max)

nums = [2,3,-2,4]
#nums = [-2,0,-1]
#nums = [-4,-3,-2]
maxProduct(nums)


