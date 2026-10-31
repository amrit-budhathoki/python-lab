# Title: Dragon Curve Fractal Text Art

# Draws a Dragon Curve fractal using recursive line-drawing with ASCII characters.
# The Dragon Curve is a famous fractal that appears in nature and mathematics.
# It's drawn by recursively replacing line segments with a right-angle pattern.

def dragon_curve(order, x, y, dx, dy, canvas):
    """Recursively draw dragon curve by replacing lines with right-angle patterns"""
    if order == 0:
        # Base case: draw a line segment
        nx, ny = x + dx, y + dy
        canvas[int(y)][int(x)] = '█'
        canvas[int(ny)][int(nx)] = '█'
        return
    
    # Recursive case: split into two segments at right angle
    # First segment: go in current direction
    dragon_curve(order - 1, x, y, dx, dy, canvas)
    
    # Second segment: turn right (rotate 90 degrees clockwise)
    # New direction is perpendicular: (dx, dy) -> (dy, -dx)
    new_dx, new_dy = dy, -dx
    new_x, new_y = x + dx, y + dy
    dragon_curve(order - 1, new_x, new_y, new_dx, new_dy, canvas)

def main():
    width, height = 80, 40
    # Initialize canvas with spaces
    canvas = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Draw dragon curve with order 12 (controls fractal detail level)
    order = 12
    start_x, start_y = 5, 20
    scale = 0.5  # Controls size of each step
    
    # Initial direction: going right
    dragon_curve(order, start_x, start_y, scale, 0, canvas)
    
    # Print the canvas
    for row in canvas:
        print(''.join(row))

if __name__ == '__main__':
    main()
