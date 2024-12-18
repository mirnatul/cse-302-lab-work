def dijkstra(graph, start):
    num_nodes = len(graph)
    distances = [float('inf')] * num_nodes
    visited = [False] * num_nodes
    distances[start] = 0

    for _ in range(num_nodes):
        min_distance = float('inf')
        min_node = -1
        for i in range(num_nodes):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                min_node = i
        visited[min_node] = True

        for neighbor, weight in enumerate(graph[min_node]):
            if weight > 0 and not visited[neighbor]:  # Check if there's an edge
                new_distance = distances[min_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    return distances

graph = [
    [0, 1, 4, 0, 0, 0],
    [1, 0, 4, 2, 7, 0],
    [4, 4, 0, 3, 5, 0],
    [0, 2, 3, 0, 4, 6],
    [0, 7, 5, 4, 0, 7],
    [0, 0, 0, 6, 7, 0]
]

start_node = 0
distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node, ":", distances)