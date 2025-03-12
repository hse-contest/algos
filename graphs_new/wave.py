from collections import defaultdict, deque

def wave_traversal(graph, start_vertex, n):
    distances = [-1] * (n + 1)
    distances[start_vertex] = 0

    queue = deque([start_vertex])
    visited = set([start_vertex])

    while queue:
        vertex = queue.popleft()

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)

    distance_groups = defaultdict(list)
    for vertex in range(1, n + 1):
        if distances[vertex] != -1:
            distance_groups[distances[vertex]].append(vertex)

    wave_order = []
    max_distance = max(distance_groups.keys())

    for distance in range(max_distance + 1):
        wave_order.extend(distance_groups[distance])

    return wave_order

n, m, v = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v_i = map(int, input().split())
    graph[u].append(v_i)
    graph[v_i].append(u)

result = wave_traversal(graph, v, n)

print(len(result))
print(' '.join(map(str, result)))
