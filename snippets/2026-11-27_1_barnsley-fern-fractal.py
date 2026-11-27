# Title: Barnsley Fern Fractal
# Generates a beautiful fern fractal using the iterated function system (IFS).
# Applies random transformations to points that converge to a self-similar leaf pattern.
# Interesting because it shows how simple rules create intricate natural-looking shapes.

import random

def barnsley_fern(iterations=50000, width=80, height=40):
    # Initialize canvas
    canvas = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Fern IFS transformations: (a, b, c, d, e, f, probability)
    transforms = [
        (0.0, 0.0, 0.0, 0.16, 0.0, 0.0, 0.01),      # Stem
        (0.85, 0.04, -0.04, 0.85, 0.0, 1.6, 0.85),  # Leaflet
        (0.2, -0.26, 0.23, 0.22, 0.0, 1.6, 0.07),   # Left frond
        (-0.15, 0.28, 0.26, 0.24, 0.0, 0.44, 0.07), # Right frond
    ]
    
    # Starting point
    x, y = 0.0, 0.0
    
    # Iterate and plot
    for _ in range(iterations):
        # Pick random transformation
        a, b, c, d, e, f, prob = random.choices(transforms, weights=[t[6] for t in transforms])[0]
        
        # Apply transformation
        x_new = a * x + b * y + e
        y_new = c * x + d * y + f
        x, y = x_new, y_new
        
        # Map to canvas (skip initial iterations for convergence)
        if _ > 100:
            # Normalize coordinates to canvas
            px = int((x + 2.5) * width / 5.0)
            py = int((10 - y) * height / 10.0)
            
            # Bounds check and plot
            if 0 <= px < width and 0 <= py < height:
                canvas[py][px] = '*'
    
    # Print canvas
    for row in canvas:
        print(''.join(row))

if __name__ == '__main__':
    barnsley_fern()
