# Title: Fireworks Display

# Launches animated fireworks across the terminal. Particles explode from random
# points and fall with gravity while fading out, creating a beautiful cascade effect.
# Interesting because it combines simple physics with ASCII art for a dynamic visual.

import random
import time
import os

class Particle:
    def __init__(self, x, y, vx, vy, char, life):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.char = char
        self.life = life
        self.max_life = life

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.1
        self.life -= 1

    def draw(self, canvas, width, height):
        if 0 <= int(self.x) < width and 0 <= int(self.y) < height:
            alpha = int((self.life / self.max_life) * 100)
            if alpha > 50:
                canvas[int(self.y)][int(self.x)] = self.char

def main():
    width, height = 80, 24
    particles = []
    colors = ['*', '+', '.', 'o', 'O']
    
    for frame in range(120):
        if frame % 8 == 0:
            cx = random.randint(10, width - 10)
            cy = random.randint(3, height - 5)
            for _ in range(40):
                angle = random.uniform(0, 2 * 3.14159)
                speed = random.uniform(1, 4)
                vx = speed * __import__('math').cos(angle)
                vy = speed * __import__('math').sin(angle)
                char = random.choice(colors)
                life = random.randint(30, 60)
                particles.append(Particle(cx, cy, vx, vy, char, life))
        
        canvas = [[' ' for _ in range(width)] for _ in range(height)]
        
        for p in particles[:]:
            p.update()
            p.draw(canvas, width, height)
            if p.life <= 0:
                particles.remove(p)
        
        os.system('clear' if os.name == 'posix' else 'cls')
        for row in canvas:
            print(''.join(row))
        
        time.sleep(0.05)

if __name__ == '__main__':
    main()
