graph = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
]

def bfs(graph, start):
    queue = [start]
    visited = {start}

    result = []

    while queue:
        cur = queue.pop(0)
        result.append(cur)

        for neighbor, edge in enumerate(graph[cur]):
            if edge == 1 and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return result

bfs(graph, 0)
