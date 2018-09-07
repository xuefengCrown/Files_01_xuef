import copy

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
    
def queens(board_size):
    def adjoin_pos(new_row, k, board):
        nb = copy.deepcopy(board) # deepcopy
        nb[new_row][k] = 1
        return nb
    
    def queen_cols(k):
        if k == 0:
            return [[[0]*8 for _ in range(8)]]
        else:
            boards = queen_cols(k-1)
            res = []
            for b in boards:
                for r in range(8):
                    if unguarded(b, r, k-1):
                        res.append(adjoin_pos(r, k-1, b))
            return res
        
    return queen_cols(board_size)
#board = [[0]*8 for _ in range(8)]
print(len(queens(8)))
        
##display(board)
##print(eight_queens(board))
#dfs(board, 0)




