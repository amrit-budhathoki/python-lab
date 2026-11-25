# Title: Dijkstra's Shortest Path Visualizer
# Shows step-by-step execution of Dijkstra's algorithm finding the shortest path
# in a graph. Watch as it explores nodes, updates distances, and builds the path.

import heapq
from collections import defaultdict

def dijkstra_visualize(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    pq = [(0, start)]
    visited = set()
    step = 0
    
    print(f"\n🎯 Finding shortest path from {start} to {end}\n")
    print(f"{'Step':<5} {'Current':<10} {'Distance':<12} {'Unvisited Queue':<30} {'All Distances':<40}")
    print("─" * 100)
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current in visited:
            continue
        
        visited.add(current)
        queue_str = str([(d, n) for d, n in pq[:3]]) if pq else "empty"
        dist_str = ", ".join(f"{n}:{distances[n]}" for n in sorted(graph.keys()))
        
        print(f"{step:<5} {current:<10} {current_dist:<12} {queue_str:<30} {dist_str:<40}")
        
        if current == end:
            print("\n✓ Destination reached!")
            break
        
        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current
                    heapq.heappush(pq, (new_dist, neighbor))
        
        step += 1
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    print(f"\n📍 Final Path: {' → '.join(path)}")
    print(f"💾 Total Distance: {distances[end]}\n")

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
    'E': [('C', 10), ('D', 2), ('F', 3)],
    'F': [('D', 6), ('E', 3)]
}

dijkstra_visualize(graph, 'A', 'F')
