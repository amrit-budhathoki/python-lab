# Title: Gravity Sandbox
# Watch particles fall and orbit around a central mass. Interesting because it demonstrates how gravity creates stable orbital mechanics from simple physics rules.

import math
import random

WIDTH, HEIGHT = 80, 24
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
GRAVITY = 0.3
DAMPING = 0.98

class Particle:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def update(self):
        dx = CENTER_X - self.x
        dy = CENTER_Y - self.y
        dist = math.sqrt(dx*dx + dy*dy) + 0.5
        
        ax = (dx / dist) * GRAVITY
        ay = (dy / dist) * GRAVITY
        
        self.vx = (self.vx + ax) * DAMPING
        self.vy = (self.vy + ay) * DAMPING
        
        self.x += self.vx
        self.y += self.vy
    
    def in_bounds(self):
        return 0 <= self.x < WIDTH and 0 <= self.y < HEIGHT

particles = []
for _ in range(30):
    angle = random.uniform(0, 2 * math.pi)
    radius = random.uniform(10, 25)
    x = CENTER_X + radius * math.cos(angle)
    y = CENTER_Y + radius * math.sin(angle)
    vx = -math.sin(angle) * random.uniform(0.3, 0.6)
    vy = math.cos(angle) * random.uniform(0.3, 0.6)
    particles.append(Particle(x, y, vx, vy))

for frame in range(200):
    canvas = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    canvas[CENTER_Y][CENTER_X] = '●'
    
    for p in particles:
        p.update()
        if p.in_bounds():
            canvas[int(p.y)][int(p.x)] = '○'
    
    print('\n'.join(''.join(row) for row in canvas))
    print(f"Frame {frame + 1}")
    if frame < 199:
        print('\033[H\033[J', end='')
