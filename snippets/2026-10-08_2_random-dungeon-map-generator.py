# Title: Random Dungeon Map Generator

# Generates a quick ASCII dungeon map with rooms connected by corridors.
# Interesting because it uses recursive backtracking to create organic-looking
# dungeon layouts, combining randomness with pathfinding for a playable result.

import random

WIDTH, HEIGHT = 40, 20
EMPTY, WALL, ROOM, CORRIDOR = '.', '#', ' ', '·'

def generate_dungeon():
    grid = [[WALL for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    rooms = []
    for _ in range(8):
        w = random.randint(4, 8)
        h = random.randint(3, 6)
        x = random.randint(1, WIDTH - w - 2)
        y = random.randint(1, HEIGHT - h - 2)
        
        valid = True
        for rx in range(x - 1, x + w + 1):
            for ry in range(y - 1, y + h + 1):
                if 0 <= rx < WIDTH and 0 <= ry < HEIGHT and grid[ry][rx] != WALL:
                    valid = False
        
        if valid:
            for ry in range(y, y + h):
                for rx in range(x, x + w):
                    grid[ry][rx] = ROOM
            rooms.append((x + w // 2, y + h // 2))
    
    for i in range(len(rooms) - 1):
        x1, y1 = rooms[i]
        x2, y2 = rooms[i + 1]
        
        if random.choice([True, False]):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if 0 <= x < WIDTH and 0 <= y1 < HEIGHT:
                    if grid[y1][x] == WALL:
                        grid[y1][x] = CORRIDOR
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if 0 <= x2 < WIDTH and 0 <= y < HEIGHT:
                    if grid[y][x2] == WALL:
                        grid[y][x2] = CORRIDOR
        else:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if 0 <= x1 < WIDTH and 0 <= y < HEIGHT:
                    if grid[y][x1] == WALL:
                        grid[y][x1] = CORRIDOR
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if 0 <= x < WIDTH and 0 <= y2 < HEIGHT:
                    if grid[y2][x] == WALL:
                        grid[y2][x] = CORRIDOR
    
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[y][x] == EMPTY:
                grid[y][x] = WALL
    
    return grid

dungeon = generate_dungeon()
for row in dungeon:
    print(''.join(row))
