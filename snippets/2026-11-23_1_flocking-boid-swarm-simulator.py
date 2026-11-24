# Title: Flocking Boid Swarm Simulator
# Simulates a flock of autonomous agents (boids) that follow simple physics rules:
# separation (avoid crowding), alignment (match velocity), and cohesion (move toward center).
# It's interesting because complex lifelike group behavior emerges from just three basic forces!

import math
import random

WIDTH, HEIGHT = 80, 24
BOID_COUNT = 15
SEPARATION_RADIUS = 5
ALIGNMENT_RADIUS = 8
COHESION_RADIUS = 10

class Boid:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
    
    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)
    
    def update(self, boids):
        # Separation: steer to avoid crowding local flockmates
        sep_x, sep_y = 0, 0
        for boid in boids:
            if boid is not self and self.distance_to(boid) < SEPARATION_RADIUS:
                sep_x += self.x - boid.x
                sep_y += self.y - boid.y
        
        # Alignment: steer towards average heading of local flockmates
        align_x, align_y, align_count = 0, 0, 0
        for boid in boids:
            if boid is not self and self.distance_to(boid) < ALIGNMENT_RADIUS:
                align_x += boid.vx
                align_y += boid.vy
                align_count += 1
        if align_count > 0:
            align_x /= align_count
            align_y /= align_count
        
        # Cohesion: steer to move toward average location of local flockmates
        coh_x, coh_y, coh_count = 0, 0, 0
        for boid in boids:
            if boid is not self and self.distance_to(boid) < COHESION_RADIUS:
                coh_x += boid.x
                coh_y += boid.y
                coh_count += 1
        if coh_count > 0:
            coh_x = coh_x / coh_count - self.x
            coh_y = coh_y / coh_count - self.y
        
        # Apply forces with weights
        self.vx += sep_x * 0.05 + align_x * 0.03 + coh_x * 0.01
        self.vy += sep_y * 0.05 + align_y * 0.03 + coh_y * 0.01
        
        # Limit speed
        speed = math.sqrt(self.vx*self.vx + self.vy*self.vy)
        if speed > 2:
            self.vx = (self.vx / speed) * 2
            self.vy = (self.vy / speed) * 2
        
        # Update position with wrapping
        self.x = (self.x + self.vx) % WIDTH
        self.y = (self.y + self.vy) % HEIGHT

boids = [Boid() for _ in range(BOID_COUNT)]

for frame in range(100):
    for boid in boids:
        boid.update(boids)
    
    grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for boid in boids:
        x, y = int(boid.x) % WIDTH, int(boid.y) % HEIGHT
        grid[y][x] = '●'
    
    print(f'\033[H\033[J', end='')
    print(f'Frame {frame} - Flocking Swarm (Boids: {BOID_COUNT})')
    for row in grid:
        print(''.join(row))
