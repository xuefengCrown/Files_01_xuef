import copy

def display(board):
    for row in board:
        print(row)

def eight_queens(board):
    return sum([sum(row) for row in board]) == 8

def unguarded(board, r, c, n):
    s = sum([board[r][i] for i in range(n)])
    s0 = sum([board[i][c] for i in range(n)])
    s1 = sum([board[r+i][c+i] for i in range(-min(r, c), n-max(r,c))])
    s2 = sum([board[i][r+c-i] for i in range(n) if r+c-i<n])
    return s+s0+s1+s2 == 0
    
def queens(board_size):
    def adjoin_pos(new_row, k, board):
        nb = copy.deepcopy(board) # deepcopy
        nb[new_row][k] = 1
        return nb
    
    def queen_cols(k, n):
        if k == 0:
            return [[[0]*n for _ in range(n)]]
        else:
            boards = queen_cols(k-1, n)
            res = []
            for b in boards:
                for r in range(n):
                    if unguarded(b, r, k-1, n):
                        res.append(adjoin_pos(r, k-1, b))
            return res
        
    boards = queen_cols(board_size, board_size)
    def trans(board, n):
        for r in range(n):
            for c in range(n): # modify in-place
                board[r][c] = 'Q' if board[r][c] == 1 else '.'
        for row in range(n):
            board[row] = ''.join(board[row])
    n = board_size
    for board in boards: trans(board, n)       
    return boards
#board = [[0]*8 for _ in range(8)]
print(queens(4))
        
##display(board)
##print(eight_queens(board))
#dfs(board, 0)




