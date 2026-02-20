from collections import deque
import heapq

def bfs(graph, start):
    """Breadth-First Search"""
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in range(len(graph[node])):
            if graph[node][neighbor] > 0 and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

def dfs(graph, start):
    """Depth-First Search"""
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            for neighbor in range(len(graph[node]) - 1, -1, -1):
                if graph[node][neighbor] > 0 and neighbor not in visited:
                    stack.append(neighbor)
    
    return result

def dijkstra(graph, start):
    """Dijkstra's Algorithm"""
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_dist, node = heapq.heappop(heap)
        
        if current_dist > distances[node]:
            continue
        
        for neighbor in range(n):
            if graph[node][neighbor] > 0:
                new_dist = current_dist + graph[node][neighbor]
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
    
    return distances