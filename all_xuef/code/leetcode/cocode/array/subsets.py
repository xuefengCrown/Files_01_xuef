"""
78. Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
    Input: nums = [1,2,3]
    Output:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
"""

"""
subset([1,2])-->subset([1,2,3])
"""
def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # [[]], 1
    def gen(old_set, new):
        return old_set + [s+[new] for s in old_set]
    # 空集的子集为 [[]]
    if len(nums) == 0: return [[]]
    return gen(subsets(nums[:len(nums)-1]), nums[-1])

nums=[1,2,3,4]
print(subsets(nums))
