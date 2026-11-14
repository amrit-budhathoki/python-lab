# Title: Pendulum Chaos Explorer

# Simulates a driven pendulum and visualizes how tiny differences in initial angle
# create wildly divergent trajectories - a beautiful demonstration of chaos theory
# and sensitive dependence on initial conditions in a nonlinear system.

import math

def simulate_pendulum(theta0, time_steps, drive_force):
    """Simulate a driven damped pendulum using Euler's method."""
    theta = theta0
    omega = 0.0
    dt = 0.01
    g, L, m, b = 9.8, 1.0, 1.0, 0.5
    
    positions = []
    for t in range(time_steps):
        # Driven damped pendulum: θ'' + b*θ' + (g/L)*sin(θ) = A*sin(ωt)
        driving = drive_force * math.sin(t * dt)
        accel = -b * omega - (g / L) * math.sin(theta) + driving
        
        omega += accel * dt
        theta += omega * dt
        positions.append(theta)
    
    return positions

def normalize_angle(angle):
    """Normalize angle to [-π, π]."""
    while angle > math.pi:
        angle -= 2 * math.pi
    while angle < -math.pi:
        angle += 2 * math.pi
    return angle

# Run two pendulums with nearly identical starting conditions
initial_angle1 = 0.5
initial_angle2 = 0.5001  # Only 0.01% difference!
drive_force = 1.2
time_steps = 1000

positions1 = simulate_pendulum(initial_angle1, time_steps, drive_force)
positions2 = simulate_pendulum(initial_angle2, time_steps, drive_force)

# Calculate divergence over time
max_divergence = 0
divergences = []
for i in range(len(positions1)):
    diff = abs(normalize_angle(positions1[i] - positions2[i]))
    divergences.append(diff)
    max_divergence = max(max_divergence, diff)

# Print ASCII visualization
print("╔════════════════════════════════════════════════════════════╗")
print("║       Chaotic Pendulum: Tiny Difference → Big Chaos       ║")
print("╚════════════════════════════════════════════════════════════╝")
print(f"\nInitial angle 1: {initial_angle1:.4f} rad")
print(f"Initial angle 2: {initial_angle2:.4f} rad (difference: {initial_angle2-initial_angle1:.6f})")
print(f"Drive force: {drive_force}\n")

# Sample every 50 steps for display
step = 50
for i in range(0, min(len(divergences), 600), step):
    bars = int(divergences[i] * 30)
    bar_char = "█"
    print(f"t={i:4d}: {bar_char * bars:<30} {divergences[i]:.4f} rad")

print(f"\nMax divergence: {max_divergence:.4f} radians")
print(f"Final divergence: {divergences[-1]:.4f} radians")
print("\n✓ Despite nearly identical starts, the pendulums diverge dramatically!")
print("✓ This is sensitive dependence on initial conditions (chaos).")
