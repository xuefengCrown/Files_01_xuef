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
    lenA, lenB = len(A), len(B)
    lenMax = max(lenA, lenB)
    dp.update([((lenMax,i),0) for i in range(lenMax+1)])
    dp.update([((i,lenMax),0) for i in range(lenMax+1)])
    maxL = 0
    # 自底向上构建表格
    for i in reversed(range(lenA)):
        for j in reversed(range(lenB)):
            dp[(i,j)] = 0
            if A[i] == B[j]:
                print("***", i,j)
                dp[(i,j)] = dp[(i+1, j+1)] + 1
                maxL = max(dp[(i,j)], maxL)
    return maxL#max(dp.values())

a = [1,2,3,2,1]
b = [3,2,1,4,7]
#a = [1,0,0,0,1]
#b = [1,0,0,1,1]
a = [0,1,1,1,1]
b = [1,0,1,0,1]
a = [0,0,0,0,0,0,1,0,0,0]
b = [0,0,0,0,0,0,0,1,0,0]

print(findLength(a,b))







                    
                
