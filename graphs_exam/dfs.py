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

def dfs(graph, start, end):
    visited = {start}
    stack = [start]
    res = []

    while stack:
        cur = stack.pop()
        res.append(cur)

        if cur == end:
            return res

        for neighbor, edge in enumerate(graph[cur]):
            if edge == 1:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

    return res

print(dfs(graph, 0, 7))
