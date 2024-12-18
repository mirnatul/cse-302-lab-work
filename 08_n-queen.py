def print_solution(board):
    for row in board:
        line = ""
        for cell in row:
            if cell == 1:
                line += "Q "
            else:
                line += ". "
        print(line)

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i in range(row - 1, -1, -1):
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False

    for i in range(row - 1, -1, -1):
        if col + (row - i) < n and board[i][col + (row - i)] == 1:
            return False
    return True

def solve_nqueens(board, row, n):
    if row == n:
        print_solution(board)
        return True

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            res = solve_nqueens(board, row + 1, n) or res
            board[row][col] = 0
    return res

def nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_nqueens(board, 0, n):
        print("No solution exists")

n = 4
nqueens(n)
