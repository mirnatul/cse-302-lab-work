def create_graph(num_vertices):
    graph = {}
    for i in range(num_vertices):
        graph[i] = []
    return graph

def add_edge(graph, src, dest):
    graph[src].append(dest)
    graph[dest].append(src)

def bfs(graph, num_vertices, start_vertex):
    visited = [False] * num_vertices
    queue = []
    visited[start_vertex] = True
    queue.append(start_vertex)

    while queue:
        current_vertex = queue.pop(0)
        print(f"Visited {current_vertex}")

        for neighbor in graph[current_vertex]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                queue.append(neighbor)


num_vertices = 6
graph = create_graph(num_vertices)
add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 1, 2)
add_edge(graph, 1, 4)
add_edge(graph, 1, 3)
add_edge(graph, 2, 4)
add_edge(graph, 3, 4)

print("BFS Traversal:")
bfs(graph, num_vertices, 0)
