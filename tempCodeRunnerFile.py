graph = create_adjacency_matrix(num_vertices)

# Add edges
add_edge_adjacency_matrix(graph, 0, 1)
add_edge_adjacency_matrix(graph, 0, 2)
add_edge_adjacency_matrix(graph, 1, 2)
add_edge_adjacency_matrix(graph, 1, 3)
add_edge_adjacency_matrix(graph, 1, 4)
add_edge_adjacency_matrix(graph, 2, 4)
add_edge_adjacency_matrix(graph, 3, 4)

print("BFS traversal starting from vertex 0:")
bfs_adjacency_matrix(graph, 0)