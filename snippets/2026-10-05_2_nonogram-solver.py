# Title: Nonogram Solver

# Solves a small nonogram (picross) puzzle using constraint satisfaction.
# Generates a random puzzle, then intelligently fills in cells by checking
# which arrangements of clues are consistent with current constraints.

from itertools import combinations

def generate_clues(row):
    """Convert a row to its nonogram clues."""
    groups = [len(g) for g in ''.join(row).split('0') if g]
    return tuple(groups) if groups else (0,)

def get_arrangements(clues, length):
    """Generate all valid arrangements for given clues and row length."""
    if clues == (0,):
        return [['0'] * length]
    
    arrangements = []
    min_space = sum(clues) + len(clues) - 1
    
    def backtrack(pos, clue_idx, current):
        if clue_idx == len(clues):
            arrangements.append(current + ['0'] * (length - pos))
            return
        
        clue = clues[clue_idx]
        remaining_clues = clues[clue_idx + 1:]
        remaining_space = sum(remaining_clues) + len(remaining_clues)
        
        for start in range(pos, length - clue - remaining_space + 1):
            new_row = current + ['0'] * (start - pos) + ['1'] * clue
            if clue_idx < len(clues) - 1:
                new_row += ['0']
                backtrack(start + clue + 1, clue_idx + 1, new_row)
            else:
                backtrack(start + clue, clue_idx + 1, new_row)
    
    backtrack(0, 0, [])
    return arrangements

def solve_nonogram(size=5):
    """Solve a nonogram puzzle."""
    solution = [['1' if (i + j) % 2 == 0 else '0' for j in range(size)] for i in range(size)]
    row_clues = [generate_clues(row) for row in solution]
    col_clues = [generate_clues([solution[i][j] for i in range(size)]) for j in range(size)]
    
    grid = [['?' for _ in range(size)] for _ in range(size)]
    
    for _ in range(20):
        for i in range(size):
            valid = [arr for arr in get_arrangements(row_clues[i], size)
                    if all(grid[i][j] == '?' or grid[i][j] == arr[j] for j in range(size))]
            
            if valid:
                for j in range(size):
                    if grid[i][j] == '?':
                        if all(arr[j] == valid[0][j] for arr in valid):
                            grid[i][j] = valid[0][j]
        
        for j in range(size):
            valid = [arr for arr in get_arrangements(col_clues[j], size)
                    if all(grid[i][j] == '?' or grid[i][j] == arr[i] for i in range(size))]
            
            if valid:
                for i in range(size):
                    if grid[i][j] == '?':
                        if all(arr[i] == valid[0][i] for arr in valid):
                            grid[i][j] = valid[0][i]
    
    return grid

grid = solve_nonogram()
print("Solved nonogram:")
for row in grid:
    print(''.join('█' if cell == '1' else '·' for cell in row))
