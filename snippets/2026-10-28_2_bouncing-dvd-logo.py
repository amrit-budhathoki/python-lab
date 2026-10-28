# Title: Bouncing DVD Logo
# A nostalgic screensaver showing a colorful DVD logo bouncing around the terminal with color changes on corner hits. Fun and mesmerizing!

import time
import os
import sys

class DVDLogo:
    def __init__(self, width=80, height=24):
        self.width = width
        self.height = height
        self.x = width // 2
        self.y = height // 2
        self.dx = 1
        self.dy = 1
        self.colors = [31, 32, 33, 34, 35, 36]  # ANSI color codes
        self.color_idx = 0
        self.logo = "DVD"
        
    def get_color(self):
        return f"\033[1;{self.colors[self.color_idx]}m"
    
    def reset_color(self):
        return "\033[0m"
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
        
        hit_corner = False
        
        if self.x <= 0 or self.x + len(self.logo) >= self.width:
            self.dx *= -1
            hit_corner = True
        
        if self.y <= 0 or self.y >= self.height - 1:
            self.dy *= -1
            hit_corner = True
        
        if hit_corner:
            self.color_idx = (self.color_idx + 1) % len(self.colors)
    
    def render(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        for i, char in enumerate(self.logo):
            if 0 <= self.x + i < self.width and 0 <= self.y < self.height:
                grid[self.y][self.x + i] = char
        
        output = self.get_color()
        for row in grid:
            output += ''.join(row) + '\n'
        output += self.reset_color()
        sys.stdout.write(output)
        sys.stdout.flush()

logo = DVDLogo()
start_time = time.time()

while time.time() - start_time < 5:
    logo.update()
    logo.render()
    time.sleep(0.05)

os.system('clear' if os.name == 'posix' else 'cls')
print("DVD logo screensaver complete!")
