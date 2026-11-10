# Title: Lenia Smooth Life Cellular Automaton
# A continuous cellular automaton that creates mesmerizing lifelike patterns.
# Unlike Conway's Game of Life with binary states, Lenia uses smooth transitions
# and kernel convolutions to produce organic, flowing structures that evolve gracefully.

import random

WIDTH, HEIGHT = 80, 24
GENERATIONS = 200
KERNEL_RADIUS = 3

def init_grid():
    return [[random.random() * 0.5 for _ in range(WIDTH)] for _ in range(HEIGHT)]

def get_neighbors(grid, y, x):
    total = 0.0
    for dy in range(-KERNEL_RADIUS, KERNEL_RADIUS + 1):
        for dx in range(-KERNEL_RADIUS, KERNEL_RADIUS + 1):
            ny = (y + dy) % HEIGHT
            nx = (x + dx) % WIDTH
            dist = ((dy**2 + dx**2) ** 0.5) / KERNEL_RADIUS
            if dist <= 1.0:
                weight = (1 - dist**2) ** 2
                total += grid[ny][nx] * weight
    return total

def growth_function(n):
    mu, sigma = 0.15, 0.015
    bell = 2.71828 ** (-((n - mu) ** 2) / (2 * sigma ** 2))
    return 2 * bell - 1

def step(grid):
    new_grid = [[0.0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            n = get_neighbors(grid, y, x)
            g = growth_function(n)
            new_grid[y][x] = max(0.0, min(1.0, grid[y][x] + 0.1 * g))
    return new_grid

def render(grid):
    chars = " ░▒▓█"
    for row in grid:
        line = "".join(chars[int(cell * 4.99)] for cell in row)
        print(line)

grid = init_grid()
print("\n" * 2)
for gen in range(GENERATIONS):
    if gen % 8 == 0:
        print(f"\rGeneration {gen}", end="", flush=True)
    grid = step(grid)

print("\n")
render(grid)
