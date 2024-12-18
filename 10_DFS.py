def create_graph(vertices):
    graph = {i: [] for i in range(vertices)}
    return graph

def add_edge(graph, src, dest):
    graph[src].append(dest)
    graph[dest].append(src)

def dfs(graph, vertex, visited):
    visited[vertex] = True
    print(f"Visited {vertex}")

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def print_graph(graph):
    for vertex, neighbors in graph.items():
        print(f"Adjacency list of vertex {vertex}: {neighbors}")

vertices = 6
graph = create_graph(vertices)

add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 1, 2)
add_edge(graph, 2, 3)
add_edge(graph, 4, 0)
add_edge(graph, 4, 1)
add_edge(graph, 4, 3)
add_edge(graph, 5, 4)

print("\nDFS traversal starting from vertex 2:")
visited = [False] * vertices 
dfs(graph, 2, visited)