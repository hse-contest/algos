graph = [
    #0  1  2  3  4  5  6  7
    [0, 1, 1, 0, 0, 0, 0, 0],  # 0
    [1, 0, 0, 1, 1, 0, 0, 0],  # 1
    [0, 0, 0, 0, 1, 1, 0, 0],  # 2
    [0, 1, 0, 0, 0, 0, 1, 0],  # 3
    [0, 0, 0, 0, 0, 0, 0, 1],  # 4
    [0, 0, 0, 0, 0, 0, 1, 0],  # 5
    [0, 0, 0, 0, 1, 0, 0, 1],  # 6
    [0, 0, 0, 0, 0, 0, 0, 0],  # 7
]
def bfs(graph, start, end):
    queue = [start]
    visited = {start}

    result = []

    while queue:
        cur = queue.pop(0)
        result.append(cur)

        if cur == end:
            return result

        for neighbor, edge in enumerate(graph[cur]):
            if edge == 1:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    return result

print(bfs(graph, 0, 7))
