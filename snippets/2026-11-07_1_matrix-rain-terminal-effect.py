# Title: Matrix Rain Terminal Effect

# A mesmerizing "Matrix" digital rain effect where characters cascade down the terminal
# in glowing columns at varying speeds. Simple but hypnotic to watch!

import time
import random
import sys

class Column:
    def __init__(self, x, height):
        self.x = x
        self.height = height
        self.y = random.randint(-height, 0)
        self.speed = random.uniform(0.5, 2.0)
        self.chars = [chr(random.randint(33, 126)) for _ in range(height)]
        self.brightness = random.randint(1, 3)
    
    def update(self, elapsed):
        self.y += self.speed * elapsed
        if self.y > self.height:
            self.y = random.randint(-self.height, 0)
            self.chars = [chr(random.randint(33, 126)) for _ in range(self.height)]
            self.brightness = random.randint(1, 3)
    
    def draw(self):
        lines = []
        for i in range(self.height):
            pos = int(self.y) + i
            if 0 <= pos < self.height:
                char = self.chars[i]
                intensity = max(0, 1.0 - (i / (self.height * 0.8)))
                lines.append((pos, self.x, char, intensity > 0.3))
        return lines

def main():
    width = 120
    height = 30
    columns = [Column(x, height) for x in range(0, width, 2)]
    
    print("\033[?25l", end="", flush=True)
    print("\033[H\033[2J", end="", flush=True)
    
    last_time = time.time()
    frame = 0
    
    try:
        while frame < 200:
            current_time = time.time()
            elapsed = current_time - last_time
            last_time = current_time
            
            for col in columns:
                col.update(elapsed)
            
            canvas = [["  " for _ in range(width // 2)] for _ in range(height)]
            
            for col in columns:
                for pos, x, char, visible in col.draw():
                    if visible and 0 <= pos < height and 0 <= x // 2 < width // 2:
                        canvas[pos][x // 2] = f"\033[32m{char} \033[0m"
            
            print("\033[H", end="", flush=True)
            for row in canvas:
                print("".join(row))
            
            time.sleep(0.03)
            frame += 1
    
    except KeyboardInterrupt:
        pass
    finally:
        print("\033[?25h", end="", flush=True)
        print("\033[2J\033[H", end="", flush=True)

if __name__ == "__main__":
    main()
