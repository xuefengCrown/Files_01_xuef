"""
64. Minimum Path Sum
"""

def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    rows = len(grid)
    cols = len(grid[0])

    dp = [[0]*cols for _ in range(rows)]

    # init tab 初始化 dp的第一行和第一列
    for i in range(cols):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    for j in range(rows):
        dp[j][0] = dp[j-1][0] + grid[j][0]

    # 逐行填充表格的余下部分
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            
    return dp[rows-1][cols-1]

grid=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
res=minPathSum(grid)
print(res)



