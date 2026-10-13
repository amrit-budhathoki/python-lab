# Title: Cyclic Color Automaton
# A cellular automaton where cells cycle through colors based on neighbors.
# Each cell advances to the next color if surrounded by the current color.
# Creates mesmerizing spiral and wave patterns that continuously evolve.

import random

WIDTH, HEIGHT = 50, 50
COLORS = ['.', 'o', '@', '#', '*']
NUM_COLORS = len(COLORS)

# Initialize random grid
grid = [[random.randint(0, NUM_COLORS - 1) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def count_color(grid, row, col, target_color):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r = (row + dr) % HEIGHT
            c = (col + dc) % WIDTH
            if grid[r][c] == target_color:
                count += 1
    return count

def step(grid):
    new_grid = [row[:] for row in grid]
    for row in range(HEIGHT):
        for col in range(WIDTH):
            current_color = grid[row][col]
            next_color = (current_color + 1) % NUM_COLORS
            # Cell advances to next color if at least 3 neighbors have current color
            if count_color(grid, row, col, current_color) >= 3:
                new_grid[row][col] = next_color
    return new_grid

def display(grid):
    print('\n' * 2)
    for row in grid:
        print(''.join(COLORS[cell] for cell in row))

# Run simulation
for generation in range(40):
    display(grid)
    grid = step(grid)
