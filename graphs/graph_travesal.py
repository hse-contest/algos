def bfs_size(graph, s):
    queue = [s]
    visited = {s}
    size = 1

    while queue:
        node = queue.pop(0)
        neighbors = graph[node]

        for neighbor in range(n):
            if neighbors[neighbor] and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                size += 1

    print(size)

n, s = map(int, input().split())
s -= 1

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

bfs_size(graph, s)
