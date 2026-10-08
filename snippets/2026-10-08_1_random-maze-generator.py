# Title: Random Maze Generator
# Generates a random maze using depth-first search and displays it as ASCII art.
# Interesting because it creates perfect mazes (one solution path) with a simple recursive algorithm.

import random

def generate_maze(width, height):
    """Generate a maze using recursive backtracking."""
    maze = [['#' for _ in range(width)] for _ in range(height)]
    
    def carve(x, y):
        maze[y][x] = ' '
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == '#':
                maze[y + dy // 2][x + dx // 2] = ' '
                carve(nx, ny)
    
    carve(1, 1)
    return maze

def display_maze(maze):
    """Print the maze to console."""
    for row in maze:
        print(''.join(row))

def add_entrance_exit(maze):
    """Add entrance at top-left and exit at bottom-right."""
    maze[0][1] = ' '
    maze[-1][-2] = ' '

width, height = 21, 11
maze = generate_maze(width, height)
add_entrance_exit(maze)
display_maze(maze)
