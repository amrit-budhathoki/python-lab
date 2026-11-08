# Title: Mandelbrot Set ASCII Renderer
# Renders an ASCII visualization of the Mandelbrot fractal set.
# Interesting because it shows how infinite mathematical complexity emerges
# from a simple iterative formula, visualized entirely in text characters.

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def render_mandelbrot(width, height, zoom, center_x, center_y, max_iter):
    chars = " .:-=+*#%@"
    
    for row in range(height):
        line = ""
        for col in range(width):
            x = center_x + (col - width/2) * zoom / (width/2)
            y = center_y + (row - height/2) * zoom / (height/2)
            
            c = complex(x, y)
            iterations = mandelbrot(c, max_iter)
            
            char_idx = min(iterations * len(chars) // max_iter, len(chars) - 1)
            line += chars[char_idx]
        
        print(line)

# Main animation loop - zoom into the fractal
width, height = 80, 40
center_x, center_y = -0.7, 0.0
max_iter = 32

print("\n" * 2)
for zoom_step in range(6):
    zoom = 2.5 * (0.5 ** zoom_step)
    print(f"Zoom level: {zoom_step + 1}/6 (zoom={zoom:.6f})")
    print("-" * width)
    render_mandelbrot(width, height, zoom, center_x, center_y, max_iter)
    print()
