# Title: Dijkstra's Shortest Path Visualizer

# Finds the shortest path in a weighted graph step-by-step using Dijkstra's algorithm.
# Watch as the algorithm explores nodes, updating distances and finding optimal routes.
# Interesting because it shows how greedy algorithms can solve global optimization problems.

import heapq
from collections import defaultdict

def dijkstra_visualize():
    # Build a small weighted graph
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)]
    }
    
    start = 'A'
    end = 'E'
    
    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parent = {node: None for node in graph}
    pq = [(0, start)]
    visited = set()
    step = 0
    
    print(f"Finding shortest path from {start} to {end}\n")
    print("=" * 60)
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current in visited:
            continue
        
        visited.add(current)
        step += 1
        
        print(f"Step {step}: Visiting {current} (distance: {current_dist})")
        
        # Explore neighbors
        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                new_dist = current_dist + weight
                
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    parent[neighbor] = current
                    heapq.heappush(pq, (new_dist, neighbor))
                    print(f"  → Update {neighbor}: {float('inf') if distances[neighbor] == float('inf') else distances[neighbor] - new_dist + distances[neighbor]} → {new_dist}")
        
        print()
    
    # Reconstruct path
    print("=" * 60)
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    
    print(f"\nShortest path: {' → '.join(path)}")
    print(f"Total distance: {distances[end]}")
    print(f"\nAll shortest distances from {start}:")
    for node in sorted(distances.keys()):
        print(f"  {start} to {node}: {distances[node]}")

dijkstra_visualize()
