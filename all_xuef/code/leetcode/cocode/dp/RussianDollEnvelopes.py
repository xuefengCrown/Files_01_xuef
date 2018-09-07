"""
354 Russian Doll Envelopes
similar: 300. Longest Increasing Subsequence

what matters?

dp[i] 表示 the maximum number of env[i:]
如何-->dp[i-1]?
"""

def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    # [[2,3], [5,4], [5,5], [6,6], [6,7], [7,7]]
    envelopes.sort()
    lenE = len(envelopes)
    dp = [1]*lenE
    # 从大到小依次考察信封
    for i in range(lenE-2,-1,-1):
        maxE = 0
        for j in range(i+1, lenE):
            if envelopes[i][0]<envelopes[j][0] and envelopes[i][1]<envelopes[j][1]:
                maxE = max(maxE, dp[j])
        dp[i] = maxE + 1       
    print(envelopes)
    print(dp)

"""
[[2,100], [3,200], [4,300], [5,250], [5,400], [5,500], [6,360], [6,370], [7,380]]

"""

env=[[5,4],[6,4],[6,7],[2,3]]
#env=[[2,3], [5,4], [5,5], [6,6], [6,7], [7,7]]
env=[[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
#env=[[46,89],[50,53],[52,68],[72,45],[77,81]]
maxEnvelopes(env)








