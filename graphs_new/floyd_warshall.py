def floyd_warshall():
    n = int(input())

    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    for row in dist:
        print(' '.join(map(str, row)))

floyd_warshall()
