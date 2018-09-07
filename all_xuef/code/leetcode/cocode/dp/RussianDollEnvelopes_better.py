"""
354 Russian Doll Envelopes
similar: 300. Longest Increasing Subsequence

what matters?

dp[i] 表示 the maximum number of env[i:]
如何-->dp[i-1]?
"""
from functools import cmp_to_key
import bisect
def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    # [[2,3], [5,4], [5,5], [6,6], [6,7], [7,7]]
    envelopes.sort(key=cmp_to_key(lambda x,y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1]))  

    dp = []
    for e in envelopes:
        i = bisect.bisect_left(dp, e[1])
        if i == len(dp):
            dp.append(e[1])
        else:
            dp[i] = e[1]
        print(dp)      
    return len(dp)
    

"""
[[2,100], [3,200], [4,300], [5,250], [5,400], [5,500], [6,360], [6,370], [7,380]]

"""

env=[[5,4],[6,4],[6,7],[2,3]]
#env=[[2,3], [5,4], [5,5], [6,6], [6,7], [7,7]]
env=[[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
#env=[[46,89],[50,53],[52,68],[72,45],[77,81]]
maxEnvelopes(env)








