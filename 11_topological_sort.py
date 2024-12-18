def topological_sort(vertices, edges):
    adj_list = {i: [] for i in range(vertices)}
    in_degree = {i: 0 for i in range(vertices)}

    for u, v in edges:
        adj_list[u].append(v)
        in_degree[v] += 1

    queue = []
    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)

    topo_order = []
    while queue:
        current = queue.pop(0)
        topo_order.append(current)

        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != vertices:
        raise ValueError("Graph has a cycle, topological sort not possible.")
    return topo_order

vertices = 6
edges = [
    (5, 2), 
    (5, 0), 
    (4, 0), 
    (4, 1), 
    (2, 3), 
    (3, 1)
]

try:
    print("Topological Sort:", topological_sort(vertices, edges))
except ValueError as e:
    print(e)
