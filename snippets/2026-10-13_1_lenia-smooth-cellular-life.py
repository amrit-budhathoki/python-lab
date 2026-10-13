# Title: Lenia - Smooth Cellular Life
# Lenia is a continuous cellular automaton that creates lifelike patterns through smooth kernels
# and continuous state values. Watch blob-like creatures evolve and move across the grid.

import math
import random

def gaussian_kernel(dist, sigma=0.15):
    """Smooth Gaussian kernel for neighborhood influence"""
    return math.exp(-(dist * dist) / (2 * sigma * sigma))

def growth_function(n):
    """Map neighborhood sum to growth value"""
    mu, sigma = 0.15, 0.015
    return 2 * math.exp(-(n - mu) ** 2 / (2 * sigma * sigma)) - 1

def simulate_lenia(width, height, steps):
    """Run Lenia cellular automaton"""
    grid = [[0.0 for _ in range(width)] for _ in range(height)]
    
    # Initialize with random seed
    for i in range(height):
        for j in range(width):
            if random.random() < 0.1:
                grid[i][j] = random.uniform(0.3, 0.7)
    
    kernel_range = 13
    
    for step in range(steps):
        new_grid = [[0.0 for _ in range(width)] for _ in range(height)]
        
        for i in range(height):
            for j in range(width):
                neighborhood_sum = 0.0
                count = 0
                
                # Calculate weighted neighborhood
                for di in range(-kernel_range, kernel_range + 1):
                    for dj in range(-kernel_range, kernel_range + 1):
                        dist = math.sqrt(di * di + dj * dj) / kernel_range
                        if dist <= 1.0:
                            ni = (i + di) % height
                            nj = (j + dj) % width
                            weight = gaussian_kernel(dist)
                            neighborhood_sum += grid[ni][nj] * weight
                            count += weight
                
                # Normalize and apply growth function
                if count > 0:
                    avg_neighborhood = neighborhood_sum / count
                    growth = growth_function(avg_neighborhood)
                    new_val = max(0.0, min(1.0, grid[i][j] + 0.1 * growth))
                    new_grid[i][j] = new_val
        
        grid = new_grid
        
        # Display every few steps
        if step % 10 == 0:
            print(f"\n--- Step {step} ---")
            for i in range(height):
                row = ""
                for j in range(width):
                    val = grid[i][j]
                    if val < 0.2:
                        row += " "
                    elif val < 0.4:
                        row += "."
                    elif val < 0.6:
                        row += "o"
                    elif val < 0.8:
                        row += "O"
                    else:
                        row += "@"
                print(row)

simulate_lenia(60, 20, 50)
