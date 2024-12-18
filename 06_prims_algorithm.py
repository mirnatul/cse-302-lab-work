def prims_algorithm_simple(graph):
    start_vertex = next(iter(graph))
    visited = set()
    mst = []
    total_cost = 0

    visited.add(start_vertex)
    
    while len(visited) < len(graph):
        min_edge = None
        
        for vertex in visited:
            for neighbor, weight in graph[vertex]:
                if neighbor not in visited:
                    if min_edge is None or weight < min_edge[2]:
                        min_edge = (vertex, neighbor, weight)
        
        if min_edge:
            from_vertex, to_vertex, weight = min_edge
            mst.append((from_vertex, to_vertex, weight))
            total_cost += weight
            visited.add(to_vertex)

    return mst, total_cost

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

mst, total_cost = prims_algorithm_simple(graph)
print("Minimum Spanning Tree:", mst)
print("Total Cost:", total_cost)
