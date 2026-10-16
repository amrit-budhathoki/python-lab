# Title: Sierpinski Triangle Fractal

# Generates a Sierpinski triangle using recursive subdivision.
# Beautiful self-similar fractal pattern emerges from simple rules,
# demonstrating how complexity grows from elegant mathematical principles.

def sierpinski(x, y, size, depth, canvas):
    if depth == 0:
        canvas[y][x] = '█'
        return
    
    half = size // 2
    sierpinski(x, y, half, depth - 1, canvas)
    sierpinski(x + half, y, half, depth - 1, canvas)
    sierpinski(x + half // 2, y + half, half, depth - 1, canvas)

def main():
    width, height = 80, 40
    canvas = [[' ' for _ in range(width)] for _ in range(height)]
    
    sierpinski(0, 0, 64, 6, canvas)
    
    for row in canvas:
        print(''.join(row))

if __name__ == '__main__':
    main()
