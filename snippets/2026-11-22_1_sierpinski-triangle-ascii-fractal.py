# Title: Sierpinski Triangle ASCII Fractal

# Generates a Sierpinski triangle using recursive subdivision.
# This classic fractal demonstrates self-similarity at every scale - each
# triangle contains smaller copies of itself, creating beautiful complexity
# from simple rules. Rendered in ASCII for instant terminal visualization.

def sierpinski(x, y, size, depth, canvas):
    """Recursively draw a Sierpinski triangle by subdividing into smaller triangles."""
    if depth == 0:
        # Base case: draw a solid triangle
        draw_triangle(x, y, size, canvas)
    else:
        # Recursive case: divide into 3 smaller triangles
        half = size // 2
        sierpinski(x, y, half, depth - 1, canvas)
        sierpinski(x + half, y, half, depth - 1, canvas)
        sierpinski(x + half // 2, y - half, half, depth - 1, canvas)

def draw_triangle(x, y, size, canvas):
    """Draw a filled triangle on the canvas using simple ASCII."""
    if size < 1:
        return
    for dy in range(size):
        for dx in range(size - dy):
            cx, cy = x + dx + dy // 2, y - dy
            if 0 <= cx < len(canvas[0]) and 0 <= cy < len(canvas):
                canvas[cy][cx] = "█"

def main():
    width, height = 128, 64
    canvas = [[" " for _ in range(width)] for _ in range(height)]
    
    # Draw Sierpinski triangle with 6 levels of recursion
    sierpinski(10, height - 5, 48, 6, canvas)
    
    # Print the canvas
    for row in canvas:
        print("".join(row))

if __name__ == "__main__":
    main()
