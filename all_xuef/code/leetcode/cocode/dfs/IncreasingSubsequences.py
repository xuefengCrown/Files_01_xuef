"""
491. Increasing Subsequences
Given an integer array, your task is to find all the different possible
increasing subsequences of the given array, and the
length of an increasing subsequence should be at least 2 .

Example:
    Input: [4, 6, 7, 7]
    Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
1. The length of the given array will not exceed 15.
2. The range of integer in the given array is [-100,100].
3. The given array may contain duplicates, and two equal integers should also
be considered as a special case of increasing sequence.
"""

def findSubsequences(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    #nums.sort()
    dp = set()
    for i in nums:
        for e in list(dp):
            if i>=e[-1]:
                dp.add(e+(i,))
        dp.add((i,))
        print(list(dp))
    return [list(e) for e in dp if len(e)>1]
nums = [4,6,7,7]
nums = [4,3,2,1]
print(findSubsequences(nums))    
