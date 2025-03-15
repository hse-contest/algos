graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 4, 'E': 2},
    'C': {'B': 1, 'D': 7},
    'D': {'E': 6},
    'E': {}
}

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

print(dijkstra(graph, 'A'))
