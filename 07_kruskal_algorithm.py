def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]

def union(parent, rank, vertex1, vertex2):
    root1 = find(parent, vertex1)
    root2 = find(parent, vertex2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

def kruskal_algorithm(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((weight, vertex, neighbor))
    
    edges.sort()

    vertices = graph.keys()
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    mst = []
    total_cost = 0

    for weight, vertex1, vertex2 in edges:
        if find(parent, vertex1) != find(parent, vertex2):
            union(parent, rank, vertex1, vertex2)
            mst.append((vertex1, vertex2, weight))
            total_cost += weight

    return mst, total_cost

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

mst, total_cost = kruskal_algorithm(graph)
print("Minimum Spanning Tree:", mst)
print("Total Cost:", total_cost)