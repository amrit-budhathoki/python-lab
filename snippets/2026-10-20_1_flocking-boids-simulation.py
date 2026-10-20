# Title: Flocking Boids Simulation
# A simple flocking simulation where autonomous agents (boids) follow three rules:
# separation (avoid crowding), alignment (match velocity), and cohesion (move toward center).
# It's interesting because complex collective behavior emerges from simple local interactions.

import math
import random

WIDTH, HEIGHT = 80, 24
NUM_BOIDS = 15
SPEED = 1.5
VISION_RANGE = 8

class Boid:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
    
    def update(self, boids):
        sep_x, sep_y = 0, 0
        align_x, align_y = 0, 0
        cohesion_x, cohesion_y = 0, 0
        count = 0
        
        for other in boids:
            if other is self:
                continue
            dx = other.x - self.x
            dy = other.y - self.y
            dist = math.sqrt(dx*dx + dy*dy)
            
            if dist < VISION_RANGE and dist > 0.1:
                sep_x -= dx / (dist + 0.1)
                sep_y -= dy / (dist + 0.1)
                align_x += other.vx
                align_y += other.vy
                cohesion_x += other.x
                cohesion_y += other.y
                count += 1
        
        if count > 0:
            align_x /= count
            align_y /= count
            cohesion_x = cohesion_x / count - self.x
            cohesion_y = cohesion_y / count - self.y
        
        self.vx += sep_x * 0.02 + (align_x - self.vx) * 0.05 + cohesion_x * 0.01
        self.vy += sep_y * 0.02 + (align_y - self.vy) * 0.05 + cohesion_y * 0.01
        
        speed = math.sqrt(self.vx**2 + self.vy**2)
        if speed > SPEED:
            self.vx = self.vx / speed * SPEED
            self.vy = self.vy / speed * SPEED
        
        self.x += self.vx
        self.y += self.vy
        
        if self.x < 0: self.x = WIDTH
        if self.x > WIDTH: self.x = 0
        if self.y < 0: self.y = HEIGHT
        if self.y > HEIGHT: self.y = 0

boids = [Boid() for _ in range(NUM_BOIDS)]

for frame in range(200):
    grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    for boid in boids:
        boid.update(boids)
        x, y = int(boid.x), int(boid.y)
        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            grid[y][x] = '●'
    
    print('\033[H\033[2J', end='')
    print('╔' + '═' * WIDTH + '╗')
    for row in grid:
        print('║' + ''.join(row) + '║')
    print('╚' + '═' * WIDTH + '╝')
    print(f'Frame: {frame}', flush=True)
