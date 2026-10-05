# Title: Conway's Game of Life Viewer
# A cellular automaton that displays living and dead cells, showing how patterns evolve
# over generations. It's visually interesting to watch the chaotic patterns settle into
# stable structures and oscillators.

import random
import time

def create_grid(width, height):
    """Create a random grid of cells"""
    return [[random.choice([True, False]) for _ in range(width)] for _ in range(height)]

def count_neighbors(grid, row, col):
    """Count live neighbors for a cell"""
    height, width = len(grid), len(grid[0])
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbor_row = (row + i) % height
            neighbor_col = (col + j) % width
            if grid[neighbor_row][neighbor_col]:
                count += 1
    return count

def next_generation(grid):
    """Calculate the next generation based on Conway's rules"""
    height, width = len(grid), len(grid[0])
    new_grid = [[False] * width for _ in range(height)]
    
    for row in range(height):
        for col in range(width):
            neighbors = count_neighbors(grid, row, col)
            alive = grid[row][col]
            
            # Apply Conway's Game of Life rules
            if alive and neighbors in (2, 3):
                new_grid[row][col] = True
            elif not alive and neighbors == 3:
                new_grid[row][col] = True
    
    return new_grid

def display_grid(grid):
    """Display the grid in the terminal"""
    print("\033[2J\033[H")  # Clear screen and move cursor to top
    for row in grid:
        line = "".join("█" if cell else "·" for cell in row)
        print(line)

# Main program
width, height = 80, 20
grid = create_grid(width, height)

print("Conway's Game of Life - Press Ctrl+C to stop\n")
time.sleep(1)

try:
    for generation in range(200):
        display_grid(grid)
        print(f"Generation: {generation}")
        grid = next_generation(grid)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nSimulation stopped.")
