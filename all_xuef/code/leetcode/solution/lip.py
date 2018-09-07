def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    dp = {}
    # 记 dp[i][j] 为从 matrix[i][j] 出发最大递增路径的值
    def lip(matrix, i, j):
        if (i, j) in dp: return dp[(i,j)]
        up, down, l, r = 0,0,0,0
        
        ijv = matrix[i][j]
        upv, downv = matrix[i-1][j] if i-1 >= 0 else ijv,  matrix[i+1][j] if i+1 < len(matrix) else ijv
        lv, rv = matrix[i][j-1] if j-1 >= 0 else ijv, matrix[i][j+1] if j+1 < len(matrix[0]) else ijv
        
        if i-1 >= 0 and upv > ijv:
            up = lip(matrix, i-1, j) 
        if i+1 < len(matrix) and downv > ijv:
            down = lip(matrix, i+1, j) 
        if j-1 >= 0 and lv > ijv:
            l = lip(matrix, i, j-1) 
        if j+1 < len(matrix[0]) and rv > ijv:
            r = lip(matrix, i, j+1)
        ij = 1 + max([up, down, l, r])
        dp[(i,j)] = ij
        return ij
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            lip(matrix, i, j)
    print(max(dp.values()))

m = [[9,9,4],[6,6,8],[2,1,1]]
m = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
longestIncreasingPath(m)
