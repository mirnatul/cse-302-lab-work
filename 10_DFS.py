# Create a graph using an adjacency list
def create_graph(vertices):
    graph = {i: [] for i in range(vertices)}  # Initialize an empty adjacency list
    return graph

# Add an edge to the graph (undirected)
def add_edge(graph, src, dest):
    graph[src].append(dest)
    graph[dest].append(src)

# DFS algorithm (recursive)
def dfs(graph, vertex, visited):
    visited[vertex] = True
    print(f"Visited {vertex}")

    # Visit all the neighbors of the current vertex
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# Print the graph (adjacency list)
def print_graph(graph):
    for vertex, neighbors in graph.items():
        print(f"Adjacency list of vertex {vertex}: {neighbors}")

# Driver code
vertices = 6  # Number of vertices
graph = create_graph(vertices)

# Add edges to the graph
add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 1, 2)
add_edge(graph, 2, 3)
add_edge(graph, 4, 0)
add_edge(graph, 4, 1)
add_edge(graph, 4, 3)
add_edge(graph, 5, 4)

# Print the graph
print_graph(graph)

# Perform DFS starting from vertex 2
print("\nDFS traversal starting from vertex 2:")
visited = [False] * vertices  # Initialize visited list
dfs(graph, 2, visited)
