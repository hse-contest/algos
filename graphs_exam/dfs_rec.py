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

def dfs(graph, start, end, visited=set()):
    visited.add(start)

    for neighbor, edge in enumerate(graph[start]):
        if edge == 1:
            if neighbor == end:
                return [neighbor]
            if neighbor not in visited:
                return [neighbor] + dfs(graph, neighbor, end, visited)
    return []

print(dfs(graph, 0, 7))
