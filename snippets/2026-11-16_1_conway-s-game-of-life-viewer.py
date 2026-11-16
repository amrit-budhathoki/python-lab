# Title: Conway's Game of Life Viewer

# A minimal implementation of Conway's Game of Life that animates on the terminal.
# It's interesting because it shows how simple rules create complex, emergent patterns.

import os
import time

def print_grid(grid, width, height):
    os.system('clear' if os.name == 'posix' else 'cls')
    for y in range(height):
        for x in range(width):
            print('█' if grid[y][x] else '·', end='')
        print()

def count_neighbors(grid, x, y, width, height):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % width, (y + dy) % height
            if grid[ny][nx]:
                count += 1
    return count

def step(grid, width, height):
    new_grid = [[False] * width for _ in range(height)]
    for y in range(height):
        for x in range(width):
            neighbors = count_neighbors(grid, x, y, width, height)
            alive = grid[y][x]
            if alive and neighbors in [2, 3]:
                new_grid[y][x] = True
            elif not alive and neighbors == 3:
                new_grid[y][x] = True
    return new_grid

width, height = 40, 20

grid = [[False] * width for _ in range(height)]

patterns = [
    [(10, 9), (10, 10), (10, 11)],
    [(20, 8), (20, 9), (20, 10), (21, 10), (22, 9)],
    [(5, 15), (6, 15), (5, 16), (6, 16)],
]

for pattern in patterns:
    for x, y in pattern:
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = True

for generation in range(60):
    print_grid(grid, width, height)
    print(f"Generation: {generation}")
    grid = step(grid, width, height)
    time.sleep(0.1)
