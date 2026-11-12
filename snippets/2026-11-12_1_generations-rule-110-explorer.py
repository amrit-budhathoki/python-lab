# Title: Generations Rule 110 Explorer
# Rule 110 is a famous elementary cellular automaton that exhibits complex behavior.
# This program visualizes how a simple rule evolves from a single cell into intricate patterns.
# It's interesting because Rule 110 is known to be Turing complete!

import random

def rule_110(left, center, right):
    """Apply Rule 110: neighborhood -> new state"""
    rules = {
        (1, 1, 1): 0,
        (1, 1, 0): 1,
        (1, 0, 1): 1,
        (1, 0, 0): 0,
        (0, 1, 1): 1,
        (0, 1, 0): 1,
        (0, 0, 1): 1,
        (0, 0, 0): 0,
    }
    return rules[(left, center, right)]

def step(grid):
    """Evolve grid by one generation"""
    width = len(grid)
    new_grid = [0] * width
    for i in range(width):
        left = grid[(i - 1) % width]
        center = grid[i]
        right = grid[(i + 1) % width]
        new_grid[i] = rule_110(left, center, right)
    return new_grid

def grid_to_string(grid):
    """Convert grid to visual representation"""
    return ''.join('█' if cell else '·' for cell in grid)

def main():
    width = 60
    generations = 35
    
    # Start with a single cell in the middle
    grid = [0] * width
    grid[width // 2] = 1
    
    print("Rule 110 Cellular Automaton")
    print("Starting from a single cell:\n")
    
    for gen in range(generations):
        print(f"Gen {gen:2d}: {grid_to_string(grid)}")
        grid = step(grid)
    
    print("\n" + "="*60)
    print("Watch how complexity emerges from a simple rule!")
    print("Rule 110 is proven to be computationally universal.")

main()
