# Title: Barnsley Fern Fractal

# Generates a beautiful fern fractal using the Barnsley fern algorithm.
# Iteratively applies random affine transformations to plot points that
# converge to a self-similar pattern - nature's own fractal blueprint!

import random

def apply_transform(x, y, choice):
    if choice < 0.01:
        return 0, 0.16 * y
    elif choice < 0.86:
        return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
    elif choice < 0.93:
        return 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
    else:
        return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

width, height = 80, 40
canvas = [[' ' for _ in range(width)] for _ in range(height)]

x, y = 0, 0
for _ in range(50000):
    x, y = apply_transform(x, y, random.random())
    
    col = int((x + 3) * width / 10)
    row = int((10 - y) * height / 11)
    
    if 0 <= col < width and 0 <= row < height:
        canvas[row][col] = '*'

for row in canvas:
    print(''.join(row))
