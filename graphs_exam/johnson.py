def bellman_ford(graph, s):
    distances = {v: float('inf') for v in graph}
    distances[s] = 0
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                distances[v] = min(distances[v], distances[u] + weight)
    for u in graph:
        for v, weight in graph[u].items():
            if distances[v] > distances[u] + weight:
                return False
    return distances

def dijkstra(graph, s):
    distances = {v: float('inf') for v in graph}
    distances[s] = 0
    pq = [(0, s)]
    visited = set()

    while pq:
        dist_u, u = min(pq)
        pq.remove((dist_u, u))
        if u in visited:
            continue
        visited.add(u)
        for v, dist_v in graph[u].items():
            new_dist = distances[u] + dist_v
            if new_dist < distances[v]:
                distances[v] = new_dist
                pq.append((new_dist, v))
    return distances

def johnson(graph):
    augmented_graph = graph.copy()
    source = 'source'
    augmented_graph[source] = {v: 0 for v in graph}

    h = bellman_ford(augmented_graph, source)

    if h is False:
        return False

    del h[source]

    reweighted_graph = {u: {} for u in graph}
    for u in graph:
        for v, weight in graph[u].items():
            reweighted_graph[u][v] = weight + h[u] - h[v]

    all_pairs_shortest_paths = {}
    for u in graph:
        reweighted_distances = dijkstra(reweighted_graph, u)

        all_pairs_shortest_paths[u] = {}
        for v in graph:
            if v in reweighted_distances:
                all_pairs_shortest_paths[u][v] = reweighted_distances[v] - h[u] + h[v]

    return all_pairs_shortest_paths

example_graph = {
    'A': {'B': -2, 'E': 3},
    'B': {'C': -1, 'D': 4},
    'C': {'D': -3, 'E': 2},
    'D': {},
    'E': {'B': 5, 'D': 1}
}

result = johnson(example_graph)

print(result)
