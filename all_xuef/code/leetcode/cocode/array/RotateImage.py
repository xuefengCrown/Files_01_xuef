"""
28. Rotate Image
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 
rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

分析：
1. 旋转的特性(分层分步旋转)

"""


# 顺时针旋转顶点的四个元素(in-place 原地)
def rtt(m, top_left, top_right, botton_left, botton_right):
    tmp = m[top_left[0]][top_left[1]]
    m[top_left[0]][top_left[1]] = m[botton_left[0]][botton_left[1]]
    m[botton_left[0]][botton_left[1]] = m[botton_right[0]][botton_right[1]]
    m[botton_right[0]][botton_right[1]] = m[top_right[0]][top_right[1]]
    m[top_right[0]][top_right[1]] = tmp
# 旋转矩阵的一整层(由四个顶点标记的那一层)
def rtt_outer(m, tl, tr, bl, br):
    top_left, top_right, botton_left, botton_right = tl[:], tr[:], bl[:], br[:]
    #[0,0],[0,sz-1],[sz-1,0],[sz-1,sz-1]
    for _ in range(tr[1]-tl[1]):
        top_left[1] += 1
        top_right[0] += 1
        botton_left[0] -= 1
        botton_right[1] -= 1
        rtt(m, top_left, top_right, botton_left, botton_right)
def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    # 一阶方阵的90°旋转还是本身
    sz = len(matrix)
    if sz<= 1: return
    tl, tr, bl, br = [0,0],[0,sz-1],[sz-1,0],[sz-1,sz-1]
    while tr[1]-tl[1] > 0:
        print(tl, tr, bl, br)
        rtt_outer(matrix, tl, tr, bl, br)
        tl[0] += 1; tl[1] += 1
        tr[0] += 1; tr[1] -= 1
        bl[0] -= 1; bl[1] += 1
        br[0] -= 1; br[1] -= 1
    
def displayMat(m):
    for r in m:
        for i in r:
            print('%2d' % i, end=" ")
        print()

matrix = [[ 5, 1, 9,11],
          [ 2, 4, 8,10],
          [13, 3, 6, 7],
          [15,14,12,16]]
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
##displayMat(matrix)
##rtt_outer(matrix)
##print("-" * 30)
##displayMat(matrix)
##
##print("*" * 30)
##sz = len(matrix)
displayMat(matrix)
print("-" * 30)
rotate(matrix)
displayMat(matrix)






