# Title: Ulam Spiral Prime Visualizer

# This program generates an Ulam spiral, a fascinating mathematical pattern where
# integers are arranged in a spiral and primes are marked. Primes mysteriously cluster
# along certain diagonals, revealing hidden structure in prime distribution!

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_ulam_spiral(size):
    grid = [[0] * size for _ in range(size)]
    x, y = size // 2, size // 2
    num = 1
    grid[y][x] = num
    num += 1
    
    steps = 1
    while num <= size * size:
        for _ in range(2):
            dx, dy = (1, 0) if steps % 2 == 1 else (0, 1)
            if steps % 4 >= 2:
                dx, dy = -dx, -dy
            
            for _ in range(steps):
                if num > size * size:
                    return grid
                x += dx
                y += dy
                if 0 <= x < size and 0 <= y < size:
                    grid[y][x] = num
                num += 1
            steps += 1
    
    return grid

def visualize_spiral(size=25):
    grid = generate_ulam_spiral(size)
    
    print("\n" + "=" * (size * 2 + 2))
    print("ULAM SPIRAL (★ = prime, · = composite)")
    print("=" * (size * 2 + 2) + "\n")
    
    for row in grid:
        line = ""
        for num in row:
            if is_prime(num):
                line += "★ "
            else:
                line += "· "
        print(line)
    
    print("\n" + "=" * (size * 2 + 2))
    
    prime_count = sum(1 for row in grid for num in row if is_prime(num))
    total = size * size
    print(f"Primes found: {prime_count} out of {total} numbers ({100*prime_count/total:.1f}%)")
    print("Notice the diagonal and straight-line patterns? That's the mystery of primes!")
    print("=" * (size * 2 + 2) + "\n")

visualize_spiral(25)
