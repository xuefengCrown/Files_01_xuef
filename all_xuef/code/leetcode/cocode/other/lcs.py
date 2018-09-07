"""
718. Maximum Length of Repeated Subarray (dynamic programming)
记 dp[i,j] 为 LCS of A[i],B[j]
1. 如果 A[i] == B[j], 则dp[i,j] = dp[i-1, j-1] + 1
2. 如果 A[i] != B[j], 则dp[i,j] = max(dp[i-1, j], dp[i, j-1])
我们可以自顶向下计算 d[i,j]; 也可以自底向上来构建 d[i,j]
"""
class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = {}
        def f(a, b, i, j):
            # base case
            if i < 0 or j < 0: return 0
            if (i,j) not in dp:
                if a[i] == b[j]: 
                    dp[(i-1, j-1)] = f(a, b, i-1, j-1)
                    dp[(i,j)] = dp[(i-1, j-1)] + 1
                else:
                    dp[(i, j-1)], dp[(i-1, j)] = f(a, b, i, j-1), f(a, b, i-1, j)
                    dp[(i,j)] = max(dp[(i, j-1)], dp[(i-1, j)])
            return dp[(i,j)]
        
        return f(A, B, len(A)-1, len(B)-1)
