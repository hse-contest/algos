def compute_edge_weight(i, j):
    return (179 * i + 719 * j) % 1000 - 500

def shortest_path(n):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0

    for i in range(1, n):
        if dist[i] == INF:
            continue

        for j in range(i + 1, min(i + 1000, n + 1)):
            weight = compute_edge_weight(i, j)
            if dist[i] + weight < dist[j]:
                dist[j] = dist[i] + weight

    return dist[n]

n = int(input())
result = shortest_path(n)
print(result)
