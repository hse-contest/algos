import heapq

num_runs = int(input())

for _ in range(num_runs):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    start = int(input())

    # Dijkstra's algorithm
    INF = 2009000999
    dist = [INF] * n
    dist[start] = 0
    visited = [False] * n

    pq = [(0, start)]

    while pq:
        d, v = heapq.heappop(pq)

        if visited[v]:
            continue

        visited[v] = True

        for neighbor, weight in graph[v]:
            if not visited[neighbor] and dist[v] + weight < dist[neighbor]:
                dist[neighbor] = dist[v] + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))

    print(*dist)
