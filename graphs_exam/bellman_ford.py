graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 4, 'E': 2},
    'C': {'B': 1, 'D': 7},
    'D': {'E': 6},
    'E': {}
}

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

print(bellman_ford(graph, 'A'))
