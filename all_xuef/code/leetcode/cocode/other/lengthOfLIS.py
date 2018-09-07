"""
300. Longest Increasing Subsequence
动态规划, 重要是空间的映射;
nums-->dp 利用索引来映射
dp[i] 表示 nums[i:]的最长递增子序列的长度

"""
def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []: return 0
        
    maxE = max(nums)
    dp = {i:0 for i in nums}
    dp[nums[-1]] = 1
    for i in reversed(nums):
        for j in range(i+1,maxE+1):
            if dp.get(j) is not None and dp[j]>0:
                dp[i] = max(dp[i], dp[j]+1)
                
        if dp[i] == 0: dp[i] = 1
    return max(dp.values())

def lengthOfLIS_better(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []: return 0
        
    dp = [1]*len(nums)
    dp[-1] = 1
    for i in reversed(range(len(nums))):
        for j in range(i+1,len(nums)):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
                print(dp)
        
    return max(dp)

nums = [10,9,2,5,3,7,101,18]
nums = [1,3,6,7,9,4,10,5,6]
print(lengthOfLIS_better(nums))
