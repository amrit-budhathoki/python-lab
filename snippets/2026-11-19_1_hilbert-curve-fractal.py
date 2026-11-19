# Title: Hilbert Curve Fractal
# Generates a beautiful space-filling Hilbert curve fractal in text, demonstrating
# how simple recursive rules can create complex self-similar patterns that wind
# through 2D space without crossing themselves.

def hilbert(order, angle=0):
    """Generate Hilbert curve as list of (x, y) coordinates"""
    if order == 0:
        return [(0, 0)]
    
    def rotate_90(points, clockwise=True):
        sign = -1 if clockwise else 1
        return [(sign * y, sign * x) for x, y in points]
    
    def translate(points, dx, dy):
        return [(x + dx, y + dy) for x, y in points]
    
    def scale(points, factor):
        return [(x * factor, y * factor) for x, y in points]
    
    prev = hilbert(order - 1, angle)
    size = 2 ** order
    
    # Build Hilbert curve from 4 recursive quadrants
    quad1 = rotate_90(prev, False)
    quad2 = translate(prev, 0, size // 2)
    quad3 = translate(prev, size // 2, size // 2)
    quad4 = rotate_90(translate(prev, size // 2, 0), True)
    
    result = quad1 + quad2 + quad3 + quad4
    return result

def render_curve(order, char='█'):
    """Render Hilbert curve as ASCII art"""
    points = hilbert(order)
    
    if not points:
        return
    
    # Find bounds
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    
    # Create canvas
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    canvas = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Place points
    for x, y in points:
        col = x - min_x
        row = y - min_y
        canvas[row][col] = char
    
    # Print
    for row in canvas:
        print(''.join(row))

# Generate and display Hilbert curves of increasing orders
for order in range(1, 5):
    print(f"\n--- Hilbert Curve Order {order} ---")
    render_curve(order)
