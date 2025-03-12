def ford_bellman(n, edges):
    dist = [float("inf")] * (n + 1)
    dist[1] = 0

    for _ in range(n - 1):
        for start, end, weight in edges:
            if dist[start] != float("inf") and dist[start] + weight < dist[end]:
                dist[end] = dist[start] + weight

    return [30000 if d == float("inf") else d for d in dist[1:]]

n, m = map(int, input().split())

edges = []
for _ in range(m):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

distances = ford_bellman(n, edges)

print(" ".join(map(str, distances)))
