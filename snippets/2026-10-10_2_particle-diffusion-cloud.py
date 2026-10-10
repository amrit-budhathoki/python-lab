# Title: Particle Diffusion Cloud

# Simulates gas particles spreading through space via random walk.
# Interesting because it visualizes how entropy increases and particles
# naturally diffuse from high to low concentration areas.

import random
import math

WIDTH, HEIGHT = 80, 24
grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Initialize particles in center
for _ in range(300):
    x = WIDTH // 2 + random.randint(-2, 2)
    y = HEIGHT // 2 + random.randint(-2, 2)
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        grid[y][x] += 1

# Simulate diffusion
for step in range(100):
    new_grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    # Each particle randomly walks
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[y][x] > 0:
                particles = grid[y][x]
                # Split particles randomly to adjacent cells
                for _ in range(particles):
                    nx = x + random.randint(-1, 1)
                    ny = y + random.randint(-1, 1)
                    nx = max(0, min(WIDTH - 1, nx))
                    ny = max(0, min(HEIGHT - 1, ny))
                    new_grid[ny][nx] += 1
    
    grid = new_grid
    
    # Render
    print(f"\033[2J\033[H Step {step + 1}/100")
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            density = grid[y][x]
            if density == 0:
                row += " "
            elif density < 2:
                row += "·"
            elif density < 5:
                row += "∘"
            elif density < 10:
                row += "●"
            else:
                row += "█"
        print(row)

print("\nDiffusion complete! Particles spread from center outward.")
