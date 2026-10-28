# Title: Orbital Mechanics Dance
# Simulates multiple bodies orbiting a central mass using gravitational physics.
# Shows emergent orbital patterns and demonstrates N-body dynamics in real-time.

import math
import random

class Body:
    def __init__(self, x, y, vx, vy, mass):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.mass = mass
        self.ax, self.ay = 0, 0
    
    def update_position(self, dt):
        self.vx += self.ax * dt
        self.vy += self.ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.ax, self.ay = 0, 0

def calculate_forces(bodies, dt):
    g = 100
    for i, body in enumerate(bodies):
        for other in bodies[:i] + bodies[i+1:]:
            dx = other.x - body.x
            dy = other.y - body.y
            dist_sq = dx*dx + dy*dy + 1
            dist = math.sqrt(dist_sq)
            f = g * body.mass * other.mass / dist_sq
            fx = f * dx / dist
            fy = f * dy / dist
            body.ax += fx / body.mass
            body.ay += fy / body.mass

def render(bodies, width=80, height=40):
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for body in bodies:
        x = int(body.x + width / 2)
        y = int(body.y + height / 2)
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = '*'
    print('\033[2J\033[H')
    print('\n'.join(''.join(row) for row in grid))

random.seed(42)
bodies = [Body(0, 0, 0, 0, 10)]

for _ in range(5):
    angle = random.uniform(0, 2*math.pi)
    dist = random.uniform(15, 25)
    x = dist * math.cos(angle)
    y = dist * math.sin(angle)
    speed = math.sqrt(bodies[0].mass / dist) * 0.8
    vx = -speed * math.sin(angle)
    vy = speed * math.cos(angle)
    bodies.append(Body(x, y, vx, vy, 0.5))

dt = 0.01
for step in range(600):
    calculate_forces(bodies, dt)
    for body in bodies:
        body.update_position(dt)
    
    if step % 10 == 0:
        render(bodies)

print("\nOrbital simulation complete!")
