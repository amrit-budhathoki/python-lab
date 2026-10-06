# Title: Prime Spiral Art
# Generates an Ulam spiral visualization showing prime number patterns
# Interesting because it reveals unexpected geometric patterns in prime distribution

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
    grid[y][x] = 1
    
    num = 2
    steps = 1
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction_idx = 0
    
    while num <= size * size:
        for _ in range(2):
            dx, dy = directions[direction_idx]
            for _ in range(steps):
                if num > size * size:
                    break
                x += dx
                y += dy
                if 0 <= x < size and 0 <= y < size:
                    grid[y][x] = num
                num += 1
            direction_idx = (direction_idx + 1) % 4
            if num > size * size:
                break
        steps += 1
    
    return grid

def visualize_spiral(grid):
    size = len(grid)
    for y in range(size):
        line = ""
        for x in range(size):
            num = grid[y][x]
            if num == 0:
                line += "  ."
            elif is_prime(num):
                line += "  *"
            else:
                line += "  ·"
        print(line)
    print()
    print(f"Grid size: {size}x{size}")
    prime_count = sum(1 for y in range(size) for x in range(size) if grid[y][x] > 0 and is_prime(grid[y][x]))
    print(f"Primes found: {prime_count} out of {size*size}")

size = 31
spiral = generate_ulam_spiral(size)
visualize_spiral(spiral)
