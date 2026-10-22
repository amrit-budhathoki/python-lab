# Title: N-Queens Solver with Visualization
# Solves the classic N-Queens puzzle by placing N queens on an NxN board so no two attack each other.
# Interesting because it demonstrates backtracking algorithm elegantly and shows all solutions with ASCII art.

def solve_n_queens(n):
    solutions = []
    board = [-1] * n
    
    def is_safe(row, col):
        for prev_row in range(row):
            prev_col = board[prev_row]
            if prev_col == col or abs(prev_row - row) == abs(prev_col - col):
                return False
        return True
    
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
    
    backtrack(0)
    return solutions

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "♛ "
            else:
                line += "· "
        print(line)
    print()

def main():
    n = 8
    print(f"Solving {n}-Queens puzzle...\n")
    solutions = solve_n_queens(n)
    
    print(f"Found {len(solutions)} solution(s)!\n")
    print(f"Showing first 3 solutions:\n")
    
    for i, solution in enumerate(solutions[:3]):
        print(f"Solution {i + 1}:")
        print_board(solution)
    
    print(f"Sample solution board positions: {solutions[0]}")
    print(f"(Row index → Column index where queen is placed)")

if __name__ == "__main__":
    main()
