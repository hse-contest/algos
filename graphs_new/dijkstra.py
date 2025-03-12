def dijkstra(graph, s, n):
    dist = {v: float('inf') for v in range(n)}
    dist[s] = 0
    visited = set()
    p_queue = [(0, s)]
    while p_queue:
        d, u = min(p_queue)
        p_queue.remove((d, u))
        if u in visited:
            continue
        visited.add(u)
        if d > dist[u]:
            continue
        for v in range(n):
            w = graph[u][v]
            new_dist = d + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                p_queue.append((new_dist, v))
    return dist

graph = []
n, s, f = map(int, input().split())
s -= 1
f -= 1

for _ in range(n):
    vertices = list(map(lambda x: int(x) if x != '-1' else float('inf'), input().split()))
    graph.append(vertices)

res = dijkstra(graph, s, n)[f]
print(-1 if res == float('inf') else res)
