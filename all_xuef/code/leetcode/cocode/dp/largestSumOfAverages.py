"""
813
dp[k][i]表示A[:i](包括 i)分成k组的最大均值和, 那么 dp[k][i] = max of dp[k-1][j] + avg(j+1, i)
"""
def largestSumOfAverages(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: float
    """
    # [9,1,2,3,9]
    lA = len(A)
    # average(i, j) = (P[j] - P[i]) / (j - i)
    P = [0]*lA # P[i] 为 sum(A[:i])
    for i in range(lA):
        P[i] = P[i-1] + A[i]
    print(P)

    dp = [0]*lA
    for i in range(lA):
        dp[i] = P[i]*1.0/(i+1)# dp[1][i]
    print(dp)
    if K==1: return dp[lA-1]
    for k in range(2, K+1):
        dp_tmp = dp[:]
        for i in range(k-1, lA): # dp[k][i]
            maxV = 0
            for j in range(k-1, i+1):
                maxV = max(maxV, dp[j-1] + (P[i]-P[j-1])*1.0/(i-j+1))
            dp_tmp[i] = maxV
        dp[:k-1] = [0]*(k-1)   
        dp[k-1:] = dp_tmp[k-1:]
        print("dp", "k=", k, dp)
A=[9,1,2,3,9]
largestSumOfAverages(A, 3)
