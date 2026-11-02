# Title: Sierpinski Triangle Fractal
# Draws a beautiful Sierpinski triangle using recursive subdivision in text.
# Interesting because it shows how complex fractals emerge from simple recursive rules,
# creating infinite detail at every level.

def sierpinski(x, y, size, depth, grid):
    """Recursively subdivide triangle into smaller Sierpinski triangles"""
    if depth == 0:
        # Base case: draw a single character at this position
        if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
            grid[y][x] = '█'
        return
    
    # Calculate three midpoints to create three smaller triangles
    half = size // 2
    
    # Top triangle
    sierpinski(x, y - half, half, depth - 1, grid)
    # Bottom-left triangle
    sierpinski(x - half, y + half, half, depth - 1, grid)
    # Bottom-right triangle
    sierpinski(x + half, y + half, half, depth - 1, grid)

def draw_fractal():
    """Main function to initialize grid and draw the fractal"""
    width, height = 120, 40
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Start from center-top, with reasonable size and depth
    start_x = width // 2
    start_y = height // 4
    size = 32
    depth = 5
    
    sierpinski(start_x, start_y, size, depth, grid)
    
    # Print the grid
    for row in grid:
        print(''.join(row))

if __name__ == '__main__':
    draw_fractal()
