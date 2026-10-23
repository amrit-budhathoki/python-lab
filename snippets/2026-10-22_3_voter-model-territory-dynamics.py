# Title: Voter Model Territory Dynamics

# A cellular automaton where each cell adopts its neighbors' opinions through voting.
# Interesting because it shows how consensus can spontaneously emerge from local interactions,
# creating organic-looking territorial patterns that shift and merge over time.

import random

WIDTH, HEIGHT = 80, 25
ITERATIONS = 200

# Initialize random opinions (0 or 1)
grid = [[random.randint(0, 1) for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Define symbols for display
symbols = ['█', '░']
colors = ['\033[44m', '\033[41m']  # Blue and red backgrounds
reset = '\033[0m'

def get_neighbors(r, c):
    """Get all 8 neighbors of a cell (with wrapping)."""
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr = (r + dr) % HEIGHT
            nc = (c + dc) % WIDTH
            yield grid[nr][nc]

def step():
    """Apply one iteration of the voter model."""
    new_grid = [[grid[r][c] for c in range(WIDTH)] for r in range(HEIGHT)]
    
    for r in range(HEIGHT):
        for c in range(WIDTH):
            # Cell adopts a random neighbor's opinion
            neighbors = list(get_neighbors(r, c))
            new_grid[r][c] = random.choice(neighbors)
    
    return new_grid

def display():
    """Print the current grid state."""
    print('\033[H\033[J')  # Clear screen and move cursor to top
    for r in range(HEIGHT):
        line = ''
        for c in range(WIDTH):
            opinion = grid[r][c]
            line += colors[opinion] + symbols[opinion] + reset
        print(line)

# Run simulation
for iteration in range(ITERATIONS):
    display()
    grid = step()
