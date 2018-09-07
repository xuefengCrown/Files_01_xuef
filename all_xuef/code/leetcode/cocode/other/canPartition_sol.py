"""
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that
the sum of elements in both subsets is equal.

Note:
1. Each of the array element will not exceed 100.
2. The array size will not exceed 200.

Example 1:
    Input: [1, 5, 11, 5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
    Input: [1, 2, 3, 5]
    Output: false
    Explanation: The array cannot be partitioned into equal sum subsets.
"""
def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # 如果 nums 的和为奇数, 则不可能划分为和相等的两部分
    sum_of_nums = sum(nums)
    if sum_of_nums % 2 != 0: return False
    
    dp = [0]
    res = set([0])
    for n in nums:
        for i in dp:
            res.add(n+i)
            print(res)
        dp = [] + list(res)

    print(dp) 
    return sum_of_nums//2 in dp

lst=[1,5,11,5]
print(canPartition(lst))










