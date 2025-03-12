def shortest_path():
    n, m, s = map(int, input().split())
    s -= 1

    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u-1, v-1, w))

    dist = [float("inf")] * n
    dist[s] = 0

    for _ in range(n-1):
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    negative_cycle = [False] * n
    for _ in range(n):
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = float("-inf")
                negative_cycle[v] = True

    changed = True
    while changed:
        changed = False
        for u, v, w in edges:
            if negative_cycle[u] and not negative_cycle[v]:
                negative_cycle[v] = True
                changed = True

    for i in range(n):
        if dist[i] == float("inf"):
            print("*")
        elif negative_cycle[i] or dist[i] == float("-inf"):
            print("-")
        else:
            print(dist[i])

shortest_path()
