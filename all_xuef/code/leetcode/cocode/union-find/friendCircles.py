"""547. Friend Circles
Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are
in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Note:
    1. N is in range [1,200].
    2. M[i][i] = 1 for all students.
    3. If M[i][j] = 1, then M[j][i] = 1.
Solution: Quick-Find"""
class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        rows = len(M)
        cols = rows
        # stus的索引表示学生id, 值表示学生所在组号
        stus = list(range(rows))
        # 扫描右上三角(对称矩阵的右上或下三角已经包含该矩阵的全部信息)
        for row in range(rows-1):
            for col in range(row+1, cols):
                if M[row][col] == 1:
                    tmp = stus[row]
                    for i in range(rows):
                        if stus[i] == tmp:
                            stus[i] = stus[col]
                        
        return len(set(stus))

M = [[1,1,0],
     [1,1,0],
     [0,0,1]]
M = [[1,1,0],
     [1,1,1],
     [0,1,1]]
sol = Solution()
print(sol.findCircleNum(M))




