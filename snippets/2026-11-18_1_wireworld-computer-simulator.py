# Title: Wireworld Computer Simulator

# Wireworld is a cellular automaton where electrons flow through copper wires.
# This simulates a simple logic gate setup showing how electrons propagate,
# demonstrating the beauty of emergent computation from simple local rules.

import random

WIDTH, HEIGHT = 40, 15
EMPTY, COPPER, ELECTRON_HEAD, ELECTRON_TAIL = '.', 'C', 'e', 't'

grid = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Draw a simple wire with an electron pulse
def draw_wire(r, c, length, direction):
    if direction == 'h':
        for i in range(length):
            if c + i < WIDTH:
                grid[r][c + i] = COPPER
    else:
        for i in range(length):
            if r + i < HEIGHT:
                grid[r + i][c] = COPPER

# Create wires and add electrons
draw_wire(3, 2, 10, 'h')
draw_wire(10, 2, 10, 'h')
draw_wire(5, 8, 5, 'v')
draw_wire(5, 8, 5, 'h')

# Start with electron heads
grid[3][3] = ELECTRON_HEAD
grid[10][3] = ELECTRON_HEAD

def count_neighbors(r, c, state):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < HEIGHT and 0 <= nc < WIDTH:
                if grid[nr][nc] == state:
                    count += 1
    return count

def step():
    new_grid = [row[:] for row in grid]
    
    for r in range(HEIGHT):
        for c in range(WIDTH):
            cell = grid[r][c]
            
            if cell == ELECTRON_HEAD:
                new_grid[r][c] = ELECTRON_TAIL
            elif cell == ELECTRON_TAIL:
                new_grid[r][c] = COPPER
            elif cell == COPPER:
                heads = count_neighbors(r, c, ELECTRON_HEAD)
                if heads == 1 or heads == 2:
                    new_grid[r][c] = ELECTRON_HEAD
    
    for r in range(HEIGHT):
        for c in range(WIDTH):
            grid[r][c] = new_grid[r][c]

def display():
    print('\033[2J\033[H')
    for row in grid:
        print(''.join(row))
    print()

for frame in range(50):
    display()
    step()
    import time
    time.sleep(0.1)
