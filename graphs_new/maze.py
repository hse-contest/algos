from collections import deque

def solve_maze(maze, start, end):
    n = len(maze)
    m = len(maze[0])

    start_x, start_y = start
    end_x, end_y = end

    start_x -= 1
    start_y -= 1
    end_x -= 1
    end_y -= 1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque([(start_y, start_x, 0)])

    visited = set([(start_y, start_x)])

    while queue:
        y, x, dist = queue.popleft()

        if y == end_y and x == end_x:
            return dist

        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] == 0 and (ny, nx) not in visited:
                visited.add((ny, nx))
                queue.append((ny, nx, dist + 1))

    return -1

n, m = map(int, input().split())

maze = []
for _ in range(n):
    row_input = input().split()
    row = [int(cell) for cell in row_input]
    maze.append(row)

start = list(map(int, input().split()))
end = list(map(int, input().split()))

result = solve_maze(maze, start, end)

print(result)
