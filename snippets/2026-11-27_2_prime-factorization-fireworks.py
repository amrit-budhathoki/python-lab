# Title: Prime Factorization Fireworks

# Visualize the prime factorization of numbers as an expanding "fireworks" display.
# Each prime factor is a particle that explodes outward with energy proportional to its size.
# Interesting because it reveals hidden structure in composite numbers through animation.

import math
import time

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def normalize_angle(idx, total):
    return (idx / total) * 2 * math.pi

def render_firework(factors, frame):
    size = 20
    canvas = [[' ' for _ in range(size * 2 + 1)] for _ in range(size + 1)]
    
    # Center
    canvas[size // 2][size] = '◉'
    
    # Plot each prime factor
    for idx, prime in enumerate(factors):
        angle = normalize_angle(idx, len(factors))
        distance = int((frame * 0.5 + 2) * math.log(prime + 1))
        distance = min(distance, size)
        
        x = int(size + distance * math.cos(angle))
        y = int(size // 2 + distance * math.sin(angle))
        
        if 0 <= y < len(canvas) and 0 <= x < len(canvas[0]):
            if prime == 2:
                char = '◆'
            elif prime == 3:
                char = '★'
            elif prime == 5:
                char = '●'
            else:
                char = '✦'
            canvas[y][x] = char
    
    return '\n'.join(''.join(row) for row in canvas)

def main():
    test_numbers = [24, 97, 210, 1001, 2024, 9999]
    
    for num in test_numbers:
        factors = prime_factors(num)
        print(f"\n{'=' * 45}")
        print(f"Number: {num} → Factors: {' × '.join(map(str, factors))}")
        print(f"{'=' * 45}\n")
        
        for frame in range(15):
            print('\033[2J\033[H')
            print(render_firework(factors, frame))
            time.sleep(0.1)
        
        time.sleep(0.5)

if __name__ == '__main__':
    main()
