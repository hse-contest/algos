from collections import deque

def find_tree_diameter(maze, n, m):
    start_cell = None
    for i in range(m):
        for j in range(n):
            if maze[i][j] == '.':
                start_cell = (i, j)
                break
        if start_cell:
            break

    if not start_cell:
        return 0

    farthest_cell, _ = find_farthest_cell(maze, start_cell, n, m)
    _, diameter = find_farthest_cell(maze, farthest_cell, n, m)

    return diameter

def find_farthest_cell(maze, start, n, m):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    queue = deque([(start, 0)])
    visited = {start}

    farthest_cell = start
    max_distance = 0

    while queue:
        cell, distance = queue.popleft()

        if distance > max_distance:
            max_distance = distance
            farthest_cell = cell

        i, j = cell
        for di, dj in directions:
            ni, nj = i + di, j + dj

            if 0 <= ni < m and 0 <= nj < n and maze[ni][nj] == '.' and (ni, nj) not in visited:
                visited.add((ni, nj))
                queue.append(((ni, nj), distance + 1))

    return farthest_cell, max_distance

n, m = map(int, input().split())
maze = []
for _ in range(m):
    maze.append(input())

print(find_tree_diameter(maze, n, m))
