# Title: Ulam Spiral Prime Visualizer

# Generates an Ulam spiral (a rectangular spiral of integers starting from 1)
# and highlights which numbers are prime. Fascinating because primes cluster
# along certain diagonal and straight lines in the spiral, revealing hidden
# patterns in prime distribution that aren't obvious in linear sequences.

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
    
    while num <= size * size:
        for _ in range(2):
            for _ in range(steps):
                if num > size * size:
                    break
                x += 1
                if 0 <= x < size and 0 <= y < size:
                    grid[y][x] = num
                    num += 1
            
            for _ in range(steps):
                if num > size * size:
                    break
                y -= 1
                if 0 <= x < size and 0 <= y < size:
                    grid[y][x] = num
                    num += 1
            
            steps += 1
    
    return grid

def visualize_spiral(grid):
    for row in grid:
        line = ""
        for num in row:
            if num == 0:
                line += "  . "
            elif is_prime(num):
                line += f"{num:3}*"
            else:
                line += f"{num:3} "
        print(line)

size = 21
spiral = generate_ulam_spiral(size)
print("Ulam Spiral (primes marked with *):\n")
visualize_spiral(spiral)

prime_count = sum(1 for row in spiral for num in row if num > 1 and is_prime(num))
total_count = size * size - 1
print(f"\nPrimes found: {prime_count} out of {total_count} ({100*prime_count/total_count:.1f}%)")
