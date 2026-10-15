# Title: Sudoku Solver with Backtracking
# Solves a hard Sudoku puzzle using constraint propagation and backtracking.
# Interesting because it demonstrates how intelligent search dramatically speeds up puzzle solving.

import random

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                candidates = [n for n in range(1, 10) if is_valid(board, row, col, n)]
                random.shuffle(candidates)
                for num in candidates:
                    board[row][col] = num
                    if solve(board):
                        return True
                    board[row][col] = 0
                return False
    return True

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Original Sudoku:")
for row in puzzle:
    print(" ".join(str(x) if x != 0 else "." for x in row))

solve(puzzle)

print("\nSolved Sudoku:")
for row in puzzle:
    print(" ".join(str(x) for x in row))
