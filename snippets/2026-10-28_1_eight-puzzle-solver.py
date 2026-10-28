# Title: Eight Puzzle Solver

# Solves the classic 8-puzzle (sliding tile puzzle) using A* search with Manhattan distance heuristic.
# Interesting because it finds the optimal solution path through a massive search space efficiently.

from collections import deque
import heapq

def manhattan_distance(state):
    """Calculate Manhattan distance heuristic"""
    distance = 0
    for i, val in enumerate(state):
        if val != 0:
            current_row, current_col = divmod(i, 3)
            target_row, target_col = divmod(val - 1, 3)
            distance += abs(current_row - target_row) + abs(current_col - target_col)
    return distance

def get_neighbors(state):
    """Generate all possible states from current state"""
    state_list = list(state)
    zero_pos = state_list.index(0)
    row, col = divmod(zero_pos, 3)
    neighbors = []
    
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = state_list[:]
            new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
            neighbors.append(tuple(new_state))
    
    return neighbors

def solve_puzzle(start_state, goal_state):
    """A* search to solve the puzzle"""
    start = tuple(start_state)
    goal = tuple(goal_state)
    
    if start == goal:
        return [start]
    
    open_set = [(manhattan_distance(start), 0, start)]
    came_from = {start: None}
    g_score = {start: 0}
    closed = set()
    
    while open_set:
        _, moves, current = heapq.heappop(open_set)
        
        if current in closed:
            continue
        
        closed.add(current)
        
        if current == goal:
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = came_from[node]
            return path[::-1]
        
        for neighbor in get_neighbors(current):
            if neighbor in closed:
                continue
            
            new_g = g_score[current] + 1
            
            if neighbor not in g_score or new_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = new_g
                f_score = new_g + manhattan_distance(neighbor)
                heapq.heappush(open_set, (f_score, new_g, neighbor))
    
    return None

def print_state(state):
    """Print puzzle state nicely"""
    for i in range(3):
        print("  " + " ".join(str(state[i*3 + j]) if state[i*3 + j] != 0 else "." for j in range(3)))

# Solve a puzzle
start = (1, 2, 3, 4, 5, 6, 7, 8, 0)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Create a solvable puzzle by shuffling
start = (1, 2, 3, 4, 0, 5, 7, 8, 6)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution = solve_puzzle(start, goal)

if solution:
    print(f"Solution found in {len(solution) - 1} moves!\n")
    for i, state in enumerate(solution[:8]):  # Show first 8 steps
        print(f"Step {i}:")
        print_state(state)
        print()
    if len(solution) > 8:
        print(f"... ({len(solution) - 8} more steps)")
else:
    print("No solution found")
