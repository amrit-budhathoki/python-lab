# Title: Pendulum Chaos Simulator

# Simulates a double pendulum system showing sensitive dependence on initial conditions.
# Two nearly identical pendulums with tiny differences in starting angle diverge dramatically,
# demonstrating chaos theory - a fundamental phenomenon in physics where small changes
# lead to vastly different outcomes.

import math
import time

def simulate_pendulum(theta1, theta2, omega1, omega2, steps, dt=0.01):
    """Simulate double pendulum physics"""
    g, L = 9.81, 1.0
    trajectory = [(theta1, theta2)]
    
    for _ in range(steps):
        sin1, cos1 = math.sin(theta1), math.cos(theta1)
        sin2, cos2 = math.sin(theta2), math.cos(theta2)
        
        delta = theta2 - theta1
        denom = 2 - math.cos(delta) ** 2
        
        accel1 = (math.sin(delta) * (omega2**2 * L * math.sin(delta) + g * sin2) - 
                  2 * sin1 * (omega1**2 * L + g * cos1 - g * cos2)) / (L * denom)
        
        accel2 = (2 * math.sin(delta) * (omega1**2 * L * sin1 + g * sin1 * cos1) +
                  omega2**2 * L * math.sin(delta) * math.cos(delta) +
                  2 * g * sin2) / (L * denom)
        
        omega1 += accel1 * dt
        omega2 += accel2 * dt
        theta1 += omega1 * dt
        theta2 += omega2 * dt
        
        trajectory.append((theta1, theta2))
    
    return trajectory

def visualize_frame(t1, t2, size=20):
    """Convert pendulum angle to 2D screen coordinates"""
    L = 5
    x1, y1 = int(size/2 + L * math.sin(t1)), int(size/2 + L * math.cos(t1))
    x2, y2 = int(x1 + L * math.sin(t2)), int(y1 + L * math.cos(t2))
    return (x1, y1), (x2, y2)

def draw_grid(pos1, pos2, pos1b, pos2b, size=20):
    """Draw two pendulums side by side"""
    grid = [['.' for _ in range(size*2 + 2)] for _ in range(size + 1)]
    
    for x1, y1 in [pos1, pos1b]:
        if 0 <= x1 < size and 0 <= y1 < size:
            grid[y1][x1] = 'o'
    
    for x2, y2 in [pos2, pos2b]:
        if 0 <= x2 < size and 0 <= y2 < size:
            grid[y2][x2 + size + 1] = 'O'
    
    return '\n'.join(''.join(row) for row in grid)

print("Double Pendulum Chaos - Two nearly identical systems diverge!")
print("Left: initial angle 0.5 rad | Right: initial angle 0.500001 rad\n")

t1_a, t2_a, w1_a, w2_a = 0.5, 0, 0, 0
t1_b, t2_b, w1_b, w2_b = 0.500001, 0, 0, 0

traj_a = simulate_pendulum(t1_a, t2_a, w1_a, w2_a, 300)
traj_b = simulate_pendulum(t1_b, t2_b, w1_b, w2_b, 300)

for i in [0, 50, 100, 150, 200, 250]:
    theta1_a, theta2_a = traj_a[i]
    theta1_b, theta2_b = traj_b[i]
    
    pos1_a, pos2_a = visualize_frame(theta1_a, theta2_a)
    pos1_b, pos2_b = visualize_frame(theta1_b, theta2_b)
    
    print(f"Step {i}:")
    print(draw_grid(pos1_a, pos2_a, pos1_b, pos2_b))
    
    diff = math.sqrt((theta1_a - theta1_b)**2 + (theta2_a - theta2_b)**2)
    print(f"Angular difference: {diff:.6f} rad\n")
    time.sleep(0.3)
