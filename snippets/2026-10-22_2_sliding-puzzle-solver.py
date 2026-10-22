# Title: Sliding Puzzle Solver

# Solves a classic 15-puzzle (sliding tile puzzle) using A* search with Manhattan
# distance heuristic. Interesting because it demonstrates how heuristic search can
# efficiently find solutions to combinatorial puzzles that would be intractable with brute force.

import heapq
from collections import defaultdict

def manhattan_distance(state, goal):
    distance = 0
    for i in range(16):
        if state[i] != 0:
            current_pos = i
            goal_pos = goal.index(state[i])
            distance += abs(current_pos // 4 - goal_pos // 4) + abs(current_pos % 4 - goal_pos % 4)
    return distance

def get_neighbors(state):
    state_list = list(state)
    zero_pos = state_list.index(0)
    neighbors = []
    
    for direction, delta in [(-4, 'U'), (4, 'D'), (-1, 'L'), (1, 'R')]:
        new_pos = zero_pos + delta
        if 0 <= new_pos < 16:
            if delta == -1 and zero_pos % 4 == 0:
                continue
            if delta == 1 and zero_pos % 4 == 3:
                continue
            new_state = state_list[:]
            new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
            neighbors.append((tuple(new_state), direction))
    
    return neighbors

def solve_puzzle(initial, goal):
    initial = tuple(initial)
    goal = tuple(goal)
    
    if initial == goal:
        return []
    
    open_set = [(0, initial)]
    came_from = {}
    g_score = defaultdict(lambda: float('inf'))
    g_score[initial] = 0
    visited = set()
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current in visited:
            continue
        visited.add(current)
        
        if current == goal:
            path = []
            while current in came_from:
                current, move = came_from[current]
                path.append(move)
            return path[::-1]
        
        for neighbor, move in get_neighbors(current):
            if neighbor in visited:
                continue
            
            tentative_g = g_score[current] + 1
            
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = (current, move)
                g_score[neighbor] = tentative_g
                f_score = tentative_g + manhattan_distance(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
    
    return None

initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15]
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

solution = solve_puzzle(initial_state, goal_state)

if solution:
    print(f"Solution found in {len(solution)} moves:")
    print(" → ".join(solution))
else:
    print("No solution exists")
