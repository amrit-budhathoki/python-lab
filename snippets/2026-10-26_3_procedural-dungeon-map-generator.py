# Title: Procedural Dungeon Map Generator

# Generates random fantasy dungeon layouts using recursive backtracking.
# Each run produces a unique maze-like dungeon with rooms and corridors.
# Interesting because it visualizes algorithmic dungeon generation used in roguelikes.

import random

def generate_dungeon(width=21, height=21):
    grid = [['#' for _ in range(width)] for _ in range(height)]
    
    def carve(x, y):
        grid[y][x] = '.'
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == '#':
                grid[y + dy // 2][x + dx // 2] = '.'
                carve(nx, ny)
    
    carve(1, 1)
    
    for _ in range(3):
        rx, ry = random.randrange(1, width, 2), random.randrange(1, height, 2)
        grid[ry][rx] = '.'
    
    return grid

def add_features(grid):
    width, height = len(grid[0]), len(grid)
    features = []
    
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if grid[y][x] == '.' and random.random() < 0.08:
                if random.random() < 0.5:
                    grid[y][x] = 'T'
                    features.append(('Treasure', x, y))
                else:
                    grid[y][x] = 'M'
                    features.append(('Monster', x, y))
    
    return features

def print_dungeon(grid, features):
    print("\n╔" + "═" * len(grid[0]) + "╗")
    for row in grid:
        print("║" + "".join(row) + "║")
    print("╚" + "═" * len(grid[0]) + "╝")
    
    print("\nLegend: . = Floor  # = Wall  T = Treasure  M = Monster")
    print(f"\nFeatures found: {len(features)}")
    for feature_type, x, y in features[:5]:
        print(f"  {feature_type} at ({x}, {y})")
    if len(features) > 5:
        print(f"  ... and {len(features) - 5} more")

def main():
    random.seed()
    print("🏰 Procedural Dungeon Generator 🏰\n")
    
    for level in range(1, 4):
        print(f"\n--- Level {level} ---")
        dungeon = generate_dungeon(25, 15)
        features = add_features(dungeon)
        print_dungeon(dungeon, features)

main()
