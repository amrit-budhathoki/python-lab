# Title: Conway's Game of Life - Glider Evolution
# Simulates Conway's Game of Life cellular automaton and tracks how many
# generations it takes for a classic "glider" pattern to complete its cycle.
# Interesting because it demonstrates emergent complexity from simple rules.

import time

def init_grid(size):
    return [[False] * size for _ in range(size)]

def add_glider(grid, x, y):
    pattern = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    for dx, dy in pattern:
        if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
            grid[x + dx][y + dy] = True

def count_neighbors(grid, x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % len(grid), (y + dy) % len(grid[0])
            if grid[nx][ny]:
                count += 1
    return count

def step(grid):
    size = len(grid)
    new_grid = init_grid(size)
    for x in range(size):
        for y in range(size):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y]:
                new_grid[x][y] = neighbors in [2, 3]
            else:
                new_grid[x][y] = neighbors == 3
    return new_grid

def grid_to_string(grid):
    return ''.join(''.join('█' if cell else '·' for cell in row) + '\n' for row in grid)

def grid_hash(grid):
    return tuple(tuple(row) for row in grid)

size = 20
grid = init_grid(size)
add_glider(grid, 2, 2)

print("Initial state:")
print(grid_to_string(grid))

seen = {grid_hash(grid): 0}
generation = 0

while generation < 200:
    grid = step(grid)
    generation += 1
    state_hash = grid_hash(grid)
    
    if state_hash in seen:
        cycle_start = seen[state_hash]
        cycle_length = generation - cycle_start
        print(f"\nGlider cycle detected!")
        print(f"Cycle repeats every {cycle_length} generations")
        print(f"(first seen at gen {cycle_start}, repeated at gen {generation})")
        print(f"\nFinal state (generation {generation}):")
        print(grid_to_string(grid))
        break
    
    seen[state_hash] = generation
    
    if generation % 50 == 0:
        print(f"Generation {generation}...")

if generation == 200:
    print(f"\nNo cycle found in 200 generations")
    print(f"Final state:")
    print(grid_to_string(grid))
