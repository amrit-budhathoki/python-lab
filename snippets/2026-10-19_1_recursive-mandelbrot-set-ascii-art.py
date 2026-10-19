# Title: Recursive Mandelbrot Set ASCII Art

# Generates a beautiful ASCII representation of the Mandelbrot fractal set.
# Recursively computes escape time for each character position, creating
# a self-similar pattern that reveals the infinite complexity of the set.

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def render_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
    chars = " .:-=+*#%@"
    result = []
    
    for y in range(height):
        row = ""
        for x in range(width):
            real = xmin + (x / width) * (xmax - xmin)
            imag = ymin + (y / height) * (ymax - ymin)
            c = complex(real, imag)
            escape_time = mandelbrot(c, max_iter)
            char_index = min(escape_time * len(chars) // max_iter, len(chars) - 1)
            row += chars[char_index]
        result.append(row)
    
    return result

def zoom_animation():
    configs = [
        (-2.5, 1.0, -1.25, 1.25, 80, 30, 20),
        (-0.8, -0.4, -0.2, 0.2, 80, 30, 40),
        (-0.748, -0.735, 0.065, 0.078, 80, 30, 60),
        (-0.7469, -0.7465, 0.1102, 0.1106, 80, 30, 80),
    ]
    
    for frame, (xmin, xmax, ymin, ymax, w, h, iters) in enumerate(configs):
        print(f"\n--- Frame {frame + 1}: Zooming into Mandelbrot Set ---\n")
        fractal = render_fractal(xmin, xmax, ymin, ymax, w, h, iters)
        for line in fractal:
            print(line)

zoom_animation()
