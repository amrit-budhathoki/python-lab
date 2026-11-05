# Title: Spiral Galaxy Generator

# Generates an animated ASCII spiral galaxy with rotating stars.
# Watches as stars orbit around a central point in a mesmerizing spiral pattern,
# creating a simple but captivating terminal animation of galactic motion.

import math
import time
import os

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def generate_galaxy(width, height, rotation):
    canvas = [[' ' for _ in range(width)] for _ in range(height)]
    center_x, center_y = width // 2, height // 2
    
    num_arms = 3
    stars_per_arm = 25
    
    for arm in range(num_arms):
        for i in range(stars_per_arm):
            angle = (i / stars_per_arm) * (2 * math.pi) + (arm * 2 * math.pi / num_arms) + rotation
            distance = 2 + (i / stars_per_arm) * 15
            
            x = int(center_x + distance * math.cos(angle))
            y = int(center_y + distance * math.sin(angle) * 0.5)
            
            if 0 <= x < width and 0 <= y < height:
                brightness = chr(ord('*') if i % 3 == 0 else (ord('.') if i % 2 == 0 else ord(':')))
                canvas[y][x] = brightness
    
    for _ in range(8):
        x = center_x + int(3 * math.cos(rotation))
        y = center_y + int(3 * math.sin(rotation) * 0.5)
        if 0 <= x < width and 0 <= y < height:
            canvas[y][x] = '#'
    
    return canvas

def render_canvas(canvas):
    return '\n'.join(''.join(row) for row in canvas)

def main():
    width, height = 80, 24
    duration = 4
    fps = 20
    frames = int(duration * fps)
    
    for frame in range(frames):
        clear_screen()
        rotation = (frame / frames) * (2 * math.pi) * 2
        canvas = generate_galaxy(width, height, rotation)
        print(render_canvas(canvas))
        print(f"\nFrame: {frame + 1}/{frames}")
        time.sleep(1 / fps)
    
    clear_screen()
    print("Galaxy animation complete!")

if __name__ == '__main__':
    main()
