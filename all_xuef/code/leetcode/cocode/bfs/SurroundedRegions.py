"""
130. Surrounded Regions

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

思路：
这题题意也略显含糊，实际上就是要将所有以O组成、但不连通到网格边缘的区域变为X。
所以我们可以先从四边上寻找连通到边缘的O的区域，将它们的O都变成Y。
剩余的所有O一定无法连通到边缘，所以可以全部变为X。最后再将所有Y变回O。

这题的测试比较tricky，上来没多想就用递归的DFS实现flood fill，结果发现run time error，栈溢出了。

这个题目用到的方法是图形学中的一个常用方法：Flood fill算法，
其实就是从一个点出发对周围区域进行目标颜色的填充。
https://zh.wikipedia.org/wiki/Flood_fill
"""
import queue
def solve(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    def dis(b):
        for r in b: print(r)
    if not board: return
    q = queue.Queue()
    # 先将边缘的O改为$
    rows, cols = len(board), len(board[0])
    for col in range(cols):
        if board[0][col] == 'O':
            board[0][col] = '$'
            q.put((0,col))
        if board[rows-1][col] == 'O':
            board[rows-1][col] = '$'
            q.put((rows-1,col))
    for row in range(rows):
        if board[row][0] == 'O':
            board[row][0] = '$'
            q.put((row,0))
        if board[row][cols-1] == 'O':
            board[row][cols-1] = '$'
            q.put((row,cols-1))
    while not q.empty():
        dollar_pos = q.get()
        r,c = dollar_pos
        for pos in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if pos[0]>=0 and pos[0]<rows and pos[1]>=0\
                    and pos[1]<cols and board[pos[0]][pos[1]]=='O':
                        q.put(pos)
                        board[pos[0]][pos[1]] = '$'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] != '$': board[r][c] = 'X'
            else: board[r][c] = 'O'
    dis(board)

    

board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]

board2 = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","O","X"]]

solve(board)















