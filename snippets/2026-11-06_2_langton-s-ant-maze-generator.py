# Title: Langton's Ant Maze Generator

# Langton's Ant is a simple cellular automaton where an ant follows two rules:
# at a white cell, turn right and flip color; at a black cell, turn left and flip color.
# Starting from a blank grid, the ant creates intricate maze-like patterns over time.
# This is interesting because complex order emerges from trivial local rules.

import time

def print_grid(grid, ant_pos, size):
    for y in range(size):
        row = ""
        for x in range(size):
            if (x, y) == ant_pos:
                row += "A"
            else:
                row += "█" if grid.get((x, y), 0) else "·"
        print(row)
    print()

def run_langton_ant(steps=10000, size=40):
    grid = {}
    x, y = size // 2, size // 2
    direction = 0
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    print("Langton's Ant - Cellular Automaton")
    print(f"Running for {steps} steps on {size}x{size} grid\n")
    
    display_interval = max(1, steps // 8)
    
    for step in range(1, steps + 1):
        current_color = grid.get((x, y), 0)
        
        if current_color == 0:
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        
        grid[(x, y)] = 1 - current_color
        
        dx, dy = directions[direction]
        x = (x + dx) % size
        y = (y + dy) % size
        
        if step % display_interval == 0:
            print(f"Step {step}/{steps}")
            print_grid(grid, (x, y), size)
            time.sleep(0.1)

run_langton_ant()
