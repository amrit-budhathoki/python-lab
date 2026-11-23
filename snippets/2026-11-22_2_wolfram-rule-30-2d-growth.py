# Title: Wolfram Rule 30 2D Growth
# A 2D expansion of Wolfram's Rule 30 cellular automaton, showing how a simple 1D rule
# creates intricate fractal patterns when applied across generations. Each row evolves
# based on its predecessor, revealing the beautiful chaos hidden in elementary rules.

import random

def apply_rule_30(left, center, right):
    """Apply Wolfram's Rule 30 to three neighboring cells."""
    patterns = {
        (1, 1, 1): 0, (1, 1, 0): 0, (1, 0, 1): 0, (1, 0, 0): 1,
        (0, 1, 1): 1, (0, 1, 0): 1, (0, 0, 1): 1, (0, 0, 0): 0
    }
    return patterns[(left, center, right)]

def evolve_generation(current):
    """Generate the next generation using Rule 30."""
    n = len(current)
    next_gen = []
    for i in range(n):
        left = current[(i - 1) % n]
        center = current[i]
        right = current[(i + 1) % n]
        next_gen.append(apply_rule_30(left, center, right))
    return next_gen

def render_grid(grid, width=80, height=30):
    """Render the cellular automaton grid as ASCII art."""
    for row in grid:
        line = ""
        for cell in row[:width]:
            line += "█" if cell else " "
        print(line)

def main():
    size = 161
    generations = 30
    grid = []
    
    # Initialize with single cell in center
    current = [0] * size
    current[size // 2] = 1
    grid.append(current[:])
    
    # Evolve for multiple generations
    for _ in range(generations):
        current = evolve_generation(current)
        grid.append(current[:])
    
    # Display results
    print("Wolfram Rule 30 - 2D Expansion")
    print("=" * 80)
    render_grid(grid)
    print("=" * 80)
    print(f"Generated {generations} generations from a single cell")
    print("Pattern expands with deterministic chaos following Rule 30")

if __name__ == "__main__":
    main()
