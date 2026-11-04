# Title: Dijkstra's Shortest Path Visualizer

# Visualizes Dijkstra's algorithm finding the shortest path in a graph.
# This classic graph algorithm is fascinating because it greedily explores
# the nearest unvisited node, efficiently finding optimal paths in weighted networks.

import heapq
from collections import defaultdict

def dijkstra_visual(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    pq = [(0, start)]
    visited = set()
    
    print(f"\n🗺️  Finding shortest path from {start} to {end}\n")
    step = 0
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current in visited:
            continue
        
        visited.add(current)
        step += 1
        
        # Visual progress
        status = "✓" if current == end else "→"
        print(f"Step {step}: Visit node '{current}' (distance: {current_dist})")
        
        if current == end:
            print(f"\n🎯 Destination reached!\n")
            break
        
        # Explore neighbors
        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current
                    heapq.heappush(pq, (new_dist, neighbor))
                    print(f"   └─ Update {neighbor}: {distances[neighbor]}")
    
    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    print(f"📍 Shortest path: {' → '.join(path)}")
    print(f"📏 Total distance: {distances[end]}\n")
    return path, distances[end]

# Create a sample weighted graph
graph = defaultdict(list)
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 2),
    ('D', 'F', 6),
    ('E', 'F', 3),
]

print("Building graph...")
for start, end, weight in edges:
    graph[start].append((end, weight))
    graph[end].append((start, weight))

# Ensure all nodes exist
for node in ['A', 'B', 'C', 'D', 'E', 'F']:
    if node not in graph:
        graph[node] = []

dijkstra_visual(graph, 'A', 'F')
