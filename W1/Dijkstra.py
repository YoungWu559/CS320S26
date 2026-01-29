def dijkstra(weight_matrix):
    """
    Find the shortest distance from node 0 to every other node.
    
    Args:
        weight_matrix: A 2D list representing the adjacency matrix.
                      weight_matrix[i][j] is the weight of edge from node i to j.
                      Use 0 for no direct edge (except diagonal which is 0 for self-loops).
    
    Returns:
        A list where distances[i] is the shortest distance from node 0 to node i.
    """
    n = len(weight_matrix)
    distances = [float('inf')] * n
    distances[0] = 0  # Distance from node 0 to itself is 0
    visited = [False] * n
    
    for _ in range(n):
        # Find the unvisited node with minimum distance
        min_distance = float('inf')
        min_node = -1
        
        for node in range(n):
            if not visited[node] and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node
        
        if min_node == -1:  # No more reachable nodes
            break
        
        visited[min_node] = True
        
        # Update distances to neighbors
        for neighbor in range(n):
            if not visited[neighbor] and weight_matrix[min_node][neighbor] != 0:
                new_distance = distances[min_node] + weight_matrix[min_node][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    
    return distances


# Example usage
if __name__ == "__main__":
    # Example weight matrix
    # 0 -> 1: 4, 0 -> 2: 2
    # 1 -> 2: 1, 1 -> 3: 5
    # 2 -> 3: 8, 2 -> 4: 10
    # 3 -> 4: 2
    
    weight_matrix = [
        [0, 4, 2, 0, 0],
        [0, 0, 1, 5, 0],
        [0, 0, 0, 8, 10],
        [0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0]
    ]
    
    result = dijkstra(weight_matrix)
    print("Shortest distances from node 0:")
    for i, dist in enumerate(result):
        print(f"Node 0 -> Node {i}: {dist}")

    for i, dist in enumerate(result):
        print(f"Node 0 -> Node {i}: {dist}")

    while (False):  # Placeholder for any future loop logic
        