from collections import deque
import heapq

class Graph:
    def __init__(self, adj_matrix):
        """Initialize graph from adjacency matrix"""
        self.adj_matrix = adj_matrix
        self.n = len(adj_matrix)
    
    def bfs(self, start):
        """Breadth-First Search"""
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in range(self.n):
                if self.adj_matrix[node][neighbor] != 0 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """Depth-First Search"""
        visited = set()
        result = []

        stack = deque([start])
        while stack:
            node = stack.pop()
            if node in visited:
                continue

            visited.add(node)
            result.append(node)

            for neighbor in range(self.n - 1, -1, -1):
                if self.adj_matrix[node][neighbor] != 0 and neighbor not in visited:
                    stack.append(neighbor)

        return result
    
    def dijkstra(self, start):
        """Dijkstra's Algorithm - returns shortest distances from start node"""
        distances = [float('inf')] * self.n
        distances[start] = 0
        pq = [(0, start)]  # (distance, node)
        
        while pq:
            curr_dist, node = heapq.heappop(pq)
            
            if curr_dist > distances[node]:
                continue
            
            for neighbor in range(self.n):
                weight = self.adj_matrix[node][neighbor]
                if weight > 0:  # Edge exists
                    distance = curr_dist + weight
                    
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(pq, (distance, neighbor))
        
        return distances


# Example usage
if __name__ == "__main__":
    # Adjacency matrix (0 means no edge)
    adj_matrix = [
        [0, 1, 4, 0],
        [0, 0, 2, 5],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]
    
    graph = Graph(adj_matrix)
    print("BFS from node 0:", graph.bfs(0))
    print("DFS from node 0:", graph.dfs(0))
    print("Dijkstra from node 0:", graph.dijkstra(0))