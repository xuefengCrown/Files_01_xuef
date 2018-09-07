"""
718. Maximum Length of Repeated Subarray (dynamic programming)
Input:
    A: [1,2,3,2,1]
    B: [3,2,1,4,7]
Output: 3
    Explanation: 
    The repeated subarray with maximum length is [3, 2, 1].

记 dp[i,j]
Since a common subarray of A and B must start at some A[i] and B[j],
let dp[i][j] be the longest common prefix of A[i:] and B[j:]
"""
def findLength(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    dp = {}
    # 计算a[i], b[j]开始的最大公共子串长度; 并将其注册进 dp 中
    def f(a, b, i, j):
        if i+1 == len(a)  or j+1 == len(b): return 1 if a[i] == b[j] else 0
        if (i,j) not in dp:
            dp[(i+1,j+1)] = f(a,b,i+1,j+1)
            
            dp[(i,j)] = 1+dp[(i+1,j+1)] if a[i] == b[j] else 0
        return dp[(i,j)]

    for i in range(len(A)):
        for j in range(len(B)):
            f(A,B,i,j)
            
    return max(dp.values())

a = [1,2,3,2,1]
b = [3,2,1,4,7]
#a = [1,0,0,0,1]
#b = [1,0,0,1,1]
a = [0,1,1,1,1]
b = [1,0,1,0,1]
a = [0,0,0,0,0,0,1,0,0,0]
b = [0,0,0,0,0,0,0,1,0,0]

print(findLength(a,b))







                    
                
