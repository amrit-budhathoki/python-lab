# Title: Particle Diffusion Simulation

# Simulates gas diffusion across a barrier using particle physics.
# Watch as randomly-moving particles spread from one side to the other,
# demonstrating entropy and equilibrium in real-time with ASCII visualization.

import random
import time

WIDTH, HEIGHT = 60, 20
PARTICLES = 150
BARRIER_X = WIDTH // 2

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
        self.x = max(0, min(WIDTH - 1, self.x))
        self.y = max(0, min(HEIGHT - 1, self.y))

# Initialize particles on left side
particles = [Particle(random.randint(0, BARRIER_X - 2), random.randint(0, HEIGHT - 1)) 
             for _ in range(PARTICLES)]

print("Particle Diffusion Simulation")
print("=" * WIDTH)

for step in range(100):
    # Move all particles
    for p in particles:
        p.move()
    
    # Create grid for visualization
    grid = [['·' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    # Draw barrier
    for y in range(HEIGHT):
        grid[y][BARRIER_X] = '║'
    
    # Place particles
    for p in particles:
        if 0 <= p.y < HEIGHT:
            grid[p.y][p.x] = '●'
    
    # Count particles on each side
    left = sum(1 for p in particles if p.x < BARRIER_X)
    right = sum(1 for p in particles if p.x > BARRIER_X)
    
    # Display
    print(f"\rStep {step:3d} | Left: {left:3d} | Right: {right:3d} | ", end='')
    
    if step % 10 == 0:
        print()
        for row in grid:
            print(''.join(row))
    else:
        print("█" * (right * 40 // PARTICLES), end='')
    
    time.sleep(0.05)

print("\n" + "=" * WIDTH)
print("Equilibrium reached! Particles distributed across both sides.")
