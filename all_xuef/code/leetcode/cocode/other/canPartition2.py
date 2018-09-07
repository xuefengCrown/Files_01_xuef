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
    # lst 是否能划分为 和为sum1 与 和为sum2 的两部分
    # 如 [5, 11, 5] --> 10~11?
    def canPartTwo(lst, sum1, sum2):
        
        if sum1<0 or sum2<0: return False

        if len(lst) == 1: return sum1==0 or sum2==0
        
        if len(lst) == 0: return sum1==0 and sum2==0
        
        first = lst[0]
        
        return canPartTwo(lst[1:], sum1-first, sum2) or canPartTwo(lst[1:], sum1, sum2-first)
    # 如果 nums 的和为奇数, 则不可能划分为和相等的两部分
    sum_of_nums = sum(nums)
    if sum_of_nums % 2 != 0: return False
    return canPartTwo(nums, sum_of_nums//2, sum_of_nums//2)
lst=[1,5,11,5]
#lst=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]
lst = [3,3,3,4,5]
lst=[66,90,7,6,32,16,2,78,69,88,85,26,3,9,58,65,30,96,11,31,99,49,63,83,79,97,20,64,81,80,25,69,9,75,23,70,26,71,25,54,1,40,41,82,32,10,26,33,50,71,5,91,59,96,9,15,46,70,26,32,49,35,80,21,34,95,51,66,17,71,28,88,46,21,31,71,42,2,98,96,40,65,92,43,68,14,98,38,13,77,14,13,60,79,52,46,9,13,25,8]
print(canPartition(lst))


"""
[11,5]-->
0~16 5~11

[5]
-11~16
0~5
-6~11
5~0
"""









