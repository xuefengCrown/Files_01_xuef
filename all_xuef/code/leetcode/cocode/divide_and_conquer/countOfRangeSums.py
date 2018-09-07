"""
327. Count of Range Sum

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.

问题的关键在哪里?
只讲代码不讲问题分析是讲不清的!
"""
#from bisect import bisect_left
import bisect
def countRangeSum(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """
    def mergeSol(sums, l, h, lower, upper):
        if l > h: return 0
        if l == h: return 1 if lower <= sums[l] <= upper else 0
        mid = (l+h)//2
        cl, cr = mergeSol(sums, l, mid, lower, upper), mergeSol(sums, mid+1, h, lower, upper)
        
        cnt = cl + cr
        # 交叉 [-2, 2] [1, 3]
        for i in range(l, mid+1):
            idx_l = bisect.bisect_left(sums[mid+1:h+1], lower+sums[i])
            idx_h = bisect.bisect_right(sums[mid+1:h+1], upper+sums[i])
            cnt += (idx_h - idx_l) if idx_h > idx_l else 0
        print(sums[l:mid+1],'***',l,'->',mid, '->',cr)
        print(sums[mid+1:h+1],'***',mid+1,'->',h, '->',cr)
        print(sums[l:h+1],'***',cnt)
        sums[l:h+1] = sorted(sums[l:h+1])
        return cnt
    sz = len(nums)
    sums = [0] * sz
    for i in range(sz): sums[i] = sums[i-1] + nums[i]
    print(sums)
    return mergeSol(sums, 0, sz-1, lower, upper)

nums = [-2,5,-1]
lower = -2
upper = 2

nums, lower, upper = [-3,1,2,-2,2,-1], -3, -1 # 7
rs = countRangeSum(nums, lower, upper)
print(rs)
