# Title: Prime Spiral Labyrinth

# This program generates a beautiful ASCII spiral where prime numbers are marked with
# special characters, creating an intricate visual pattern. It's interesting because it
# reveals the mysterious distribution patterns of primes in a spatial arrangement.

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

def spiral_coordinates(n):
    """Generate coordinates for numbers 1 to n in a square spiral pattern."""
    coords = {1: (0, 0)}
    x, y = 0, 0
    dx, dy = 1, 0
    steps_in_direction = 1
    step_count = 0
    direction_changes = 0
    
    for num in range(2, n + 1):
        x += dx
        y += dy
        coords[num] = (x, y)
        step_count += 1
        
        if step_count == steps_in_direction:
            step_count = 0
            dx, dy = -dy, dx
            direction_changes += 1
            if direction_changes % 2 == 0:
                steps_in_direction += 1
    
    return coords

def render_spiral(limit=200):
    """Render a spiral with primes marked distinctly."""
    coords = spiral_coordinates(limit)
    
    min_x = min(c[0] for c in coords.values())
    max_x = max(c[0] for c in coords.values())
    min_y = min(c[1] for c in coords.values())
    max_y = max(c[1] for c in coords.values())
    
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    
    grid = [['·' for _ in range(width)] for _ in range(height)]
    
    for num in range(1, limit + 1):
        x, y = coords[num]
        grid_x = x - min_x
        grid_y = y - min_y
        
        if is_prime(num):
            if num == 2:
                grid[grid_y][grid_x] = '█'
            elif num % 10 == 1:
                grid[grid_y][grid_x] = '◆'
            else:
                grid[grid_y][grid_x] = '●'
        elif num == 1:
            grid[grid_y][grid_x] = '◎'
    
    for row in grid:
        print(''.join(row))
    
    prime_count = sum(1 for i in range(1, limit + 1) if is_prime(i))
    print(f"\n✨ Spiral complete! Found {prime_count} primes among {limit} numbers")
    print("Legend: ◎=1, ●=prime, ◆=prime ending in 1, █=2, ·=composite")

render_spiral(200)
