# Title: Orbital Mechanics Simulator

# Simulates gravitational orbits of planets around a star using Newton's laws.
# Watch as celestial bodies follow realistic elliptical paths, demonstrating
# how gravity creates stable orbits and chaotic interactions.

import math
import time

class Body:
    def __init__(self, x, y, vx, vy, mass, char):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.mass = mass
        self.char = char
    
    def apply_force(self, fx, fy, dt):
        ax, ay = fx / self.mass, fy / self.mass
        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt

def calculate_gravity(b1, b2, g=1.0):
    dx = b2.x - b1.x
    dy = b2.y - b1.y
    dist_sq = dx*dx + dy*dy + 0.1
    dist = math.sqrt(dist_sq)
    force = g * b1.mass * b2.mass / dist_sq
    fx = force * dx / dist
    fy = force * dy / dist
    return fx, fy

def render(bodies, width=60, height=20):
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for body in bodies:
        x = int((body.x + 50) % 100 * width / 100)
        y = int((body.y + 50) % 100 * height / 100)
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = body.char
    print('\n'.join(''.join(row) for row in grid))
    print()

star = Body(50, 50, 0, 0, 100, '*')
planet1 = Body(70, 50, 0, -2.5, 1, 'o')
planet2 = Body(30, 50, 0, 2.0, 1, 'O')

bodies = [star, planet1, planet2]
dt = 0.05

for step in range(200):
    for body in bodies:
        fx, fy = 0, 0
        for other in bodies:
            if body is not other:
                f_x, f_y = calculate_gravity(body, other)
                fx += f_x
                fy += f_y
        body.apply_force(fx, fy, dt)
    
    if step % 5 == 0:
        print(f"Step {step}")
        render(bodies)
        time.sleep(0.05)
