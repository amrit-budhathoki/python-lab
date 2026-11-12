# Title: Menger Sponge 3D Slice

# Renders a 2D cross-section of the famous Menger Sponge fractal.
# The Menger Sponge is a 3D fractal created by recursively removing the center
# cube from a 3x3x3 grid. This program shows a horizontal slice through it,
# creating an intricate recursive pattern similar to a Sierpinski carpet variant.

def menger_slice(x, y, depth=4):
    """Check if point (x,y) is inside the Menger sponge slice"""
    for _ in range(depth):
        # Map to 0-3 range
        x_local = (x % 3)
        y_local = (y % 3)
        
        # Center cube is removed
        if x_local == 1 and y_local == 1:
            return False
        
        # Subdivide
        x /= 3
        y /= 3
    
    return True

def draw_menger(width=80, height=40, scale=2.0):
    """Draw the Menger sponge slice with ASCII characters"""
    for row in range(height):
        line = ""
        for col in range(width):
            # Map screen coordinates to mathematical space
            x = col * scale / width
            y = row * scale / height
            
            # Check if point is in the fractal
            if menger_slice(x, y):
                line += "█"
            else:
                line += " "
        
        print(line)

# Alternative recursive approach for comparison
def sierpinski_carpet(n, size=3):
    """Generate Sierpinski carpet pattern recursively"""
    if n == 0:
        return [["*"]]
    
    prev = sierpinski_carpet(n - 1)
    prev_size = len(prev)
    new_size = prev_size * 3
    result = [["." for _ in range(new_size)] for _ in range(new_size)]
    
    # Place 8 copies (skipping center)
    positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
    for dy, dx in positions:
        for i in range(prev_size):
            for j in range(prev_size):
                result[dy * prev_size + i][dx * prev_size + j] = prev[i][j]
    
    return result

print("=== Menger Sponge Slice ===\n")
draw_menger(width=100, height=50, scale=3.0)

print("\n\n=== Sierpinski Carpet ===\n")
carpet = sierpinski_carpet(4)
for row in carpet:
    print("".join(row))
