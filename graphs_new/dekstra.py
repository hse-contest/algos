def dijkstra(graph, start, end):
    n = len(graph)
    dist = [float('inf')] * n
    visited = [False] * n
    prev = [-1] * n

    dist[start - 1] = 0

    for _ in range(n):
        min_dist = float('inf')
        min_idx = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_idx = i

        if min_idx == -1 or min_idx == end - 1:
            break

        visited[min_idx] = True

        for i in range(n):
            if graph[min_idx][i] >= 0 and not visited[i]:
                new_dist = dist[min_idx] + graph[min_idx][i]
                if new_dist < dist[i]:
                    dist[i] = new_dist
                    prev[i] = min_idx

    if dist[end - 1] == float('inf'):
        return [-1]

    path = []
    curr = end - 1
    while curr != -1:
        path.append(curr + 1)
        curr = prev[curr]

    path.reverse()

    return path

n, s, f = map(int, input().split())

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

path = dijkstra(graph, s, f)

if path[0] == -1:
    print(-1)
else:
    print(" ".join(map(str, path)))
