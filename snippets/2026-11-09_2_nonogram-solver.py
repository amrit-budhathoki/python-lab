# Title: Nonogram Solver
# Solves nonogram (picross) puzzles by finding which cells must be filled.
# Uses constraint propagation to deduce cell states from line clues without brute force.

from itertools import combinations

def generate_line_possibilities(length, clues):
    """Generate all valid arrangements of filled cells for a line given clues."""
    if not clues:
        return [tuple([0] * length)]
    
    possibilities = []
    total_filled = sum(clues)
    min_space = len(clues) - 1
    
    def place_groups(pos, group_idx, current):
        if group_idx == len(clues):
            possibilities.append(tuple(current + [0] * (length - pos)))
            return
        
        group_size = clues[group_idx]
        remaining_groups = len(clues) - group_idx - 1
        remaining_filled = sum(clues[group_idx + 1:])
        min_needed = remaining_filled + remaining_groups
        
        for start in range(pos, length - group_size - min_needed + 1):
            new_current = current + [0] * (start - pos) + [1] * group_size
            if group_idx < len(clues) - 1:
                new_current.append(0)
                place_groups(start + group_size + 1, group_idx + 1, new_current)
            else:
                place_groups(start + group_size, group_idx + 1, new_current)
    
    place_groups(0, 0, [])
    return possibilities

def solve_nonogram(rows_clues, cols_clues):
    """Solve nonogram using constraint propagation."""
    height, width = len(rows_clues), len(cols_clues)
    grid = [[None] * width for _ in range(height)]
    
    changed = True
    iterations = 0
    max_iterations = 100
    
    while changed and iterations < max_iterations:
        changed = False
        iterations += 1
        
        for i in range(height):
            possibilities = [p for p in generate_line_possibilities(width, rows_clues[i])
                           if all(grid[i][j] is None or grid[i][j] == p[j] for j in range(width))]
            
            for j in range(width):
                if grid[i][j] is None:
                    values = set(p[j] for p in possibilities)
                    if len(values) == 1:
                        grid[i][j] = values.pop()
                        changed = True
        
        for j in range(width):
            possibilities = [p for p in generate_line_possibilities(height, cols_clues[j])
                           if all(grid[i][j] is None or grid[i][j] == p[i] for i in range(height))]
            
            for i in range(height):
                if grid[i][j] is None:
                    values = set(p[i] for p in possibilities)
                    if len(values) == 1:
                        grid[i][j] = values.pop()
                        changed = True
    
    return grid

def print_grid(grid):
    """Display the solved nonogram."""
    for row in grid:
        print(''.join(['█' if cell == 1 else '░' for cell in row]))

rows = [[1], [3], [1, 1], [3], [1]]
cols = [[3], [1, 1], [5], [1, 1], [3]]

solution = solve_nonogram(rows, cols)
print("Solved Nonogram:")
print_grid(solution)
