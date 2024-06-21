def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col, N):
    # Base case: If all queens are placed
    if col >= N:
        return N
    
    max_queens = col
    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1
            
            # Recur to place rest of the queens
            max_queens = max(max_queens, solve_n_queens_util(board, col + 1, N))
            
            # If placing queen in board[i][col] doesn't lead to a solution, then backtrack
            board[i][col] = 0
    
    return max_queens

def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    return solve_n_queens_util(board, 0, N)

# Example usage:
N = 8
max_queens = solve_n_queens(N)
print(max_queens)

