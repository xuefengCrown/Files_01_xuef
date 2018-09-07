def display(board):
    for row in board:
        print(row)

def eight_queens(board):
    return sum([sum(row) for row in board]) == 8

def unguarded(board, r, c):
    s = sum([board[r][i] for i in range(8)])
    s0 = sum([board[i][c] for i in range(8)])
    s1 = sum([board[r+i][c+i] for i in range(-min(r, c), 8-max(r,c))])
    s2 = sum([board[i][r+c-i] for i in range(8) if r+c-i<8])
    return s+s0+s1+s2 == 0
    
def dfs(board, col):
    if eight_queens(board):
        display(board)
        return True
    else:
        for row in range(len(board)):
            if unguarded(board, row, col):
                board[row][col] = 1
                if dfs(board, col+1):
                    return True
                else:
                    board[row][col] = 0
    return False

board = [[0]*8 for _ in range(8)]

        
##display(board)
##print(eight_queens(board))
dfs(board, 0)




