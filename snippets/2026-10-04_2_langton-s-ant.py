# Title: Langton's Ant
# A 2D cellular automaton where an ant walks on a grid, flipping cell colors based on simple rules.
# Interesting because complex patterns emerge from just 4 simple rules, creating spirals and highways.

import random

def run_langtons_ant(steps=50000, grid_size=80):
    # Initialize grid (False = white, True = black)
    grid = [[False] * grid_size for _ in range(grid_size)]
    
    # Ant position and direction (0=up, 1=right, 2=down, 3=left)
    x, y = grid_size // 2, grid_size // 2
    direction = 0
    
    # Direction vectors: up, right, down, left
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    for _ in range(steps):
        # Get current cell color
        is_black = grid[y][x]
        
        # Apply Langton's ant rules:
        # If on white: turn right (clockwise), flip to black
        # If on black: turn left (counter-clockwise), flip to white
        if is_black:
            direction = (direction - 1) % 4  # Turn left
        else:
            direction = (direction + 1) % 4  # Turn right
        
        # Flip the cell
        grid[y][x] = not grid[y][x]
        
        # Move forward
        x = (x + dx[direction]) % grid_size
        y = (y + dy[direction]) % grid_size
    
    return grid

def display_grid(grid):
    for row in grid:
        print(''.join('█' if cell else '·' for cell in row))

# Run the simulation
print("Langton's Ant - creating patterns through simple rules...")
final_grid = run_langtons_ant(steps=40000, grid_size=60)
display_grid(final_grid)
print("\n█ = black cell, · = white cell")
