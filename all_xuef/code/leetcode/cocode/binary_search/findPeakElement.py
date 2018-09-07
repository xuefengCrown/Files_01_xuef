"""
log时间复杂度算法在于只需找到一个 peak ele
If X is not a peak ele, X is at least smaller than one of its neighbours
1. if X is smaller than the left
we can find a peak ele on left
2. if X is smaller than the right
we can find a peak ele on right
!!! nums[-1] = nums[n] = -∞
"""
def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1: return 0
    def check(nums, idx):
        if idx==0:
            return nums[0]>nums[1]
        if idx==len(nums)-1:
            return nums[len(nums)-1]>nums[len(nums)-2]
        return nums[idx]>nums[idx-1] and nums[idx]>nums[idx+1]
    def helper(nums, lo, hi):
        mid = (lo + hi)//2
        if check(nums, mid): return mid

        if mid == 0: return helper(nums, mid+1, hi)
        if mid == len(nums)-1: return helper(nums, lo, mid-1)
        elif nums[mid] < nums[mid-1]:
            return helper(nums, lo, mid-1)
        else:
            return helper(nums, mid+1, hi)
    
    return helper(nums, 0, len(nums)-1)

nums=[1,2,3,1]
nums=[1,2,1,3,5,6,4]
rs=findPeakElement(nums)
print(rs)
