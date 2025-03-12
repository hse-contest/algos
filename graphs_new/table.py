from collections import deque

def min_dist(grid, n, m):
    result = [[float('inf')] * m for _ in range(n)]

    queue = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                queue.append((i, j))
                result[i][j] = 0

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and result[nx][ny] > result[x][y] + 1:
                result[nx][ny] = result[x][y] + 1
                queue.append((nx, ny))

    return result

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

distances = min_dist(grid, n, m)

for row in distances:
    print(*row)
