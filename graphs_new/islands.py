import heapq

def dijkstra(graph, city_owners, start, end):
    n = len(graph)

    distances = [float('inf')] * n
    distances[start] = 0

    paths = [[] for _ in range(n)]
    paths[start] = [start]

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)

        if current_distance > distances[current_city]:
            continue

        for neighbor in graph[current_city]:
            toll = 1 if city_owners[current_city] != city_owners[neighbor] else 0

            new_distance = current_distance + toll

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                paths[neighbor] = paths[current_city] + [neighbor]
                heapq.heappush(priority_queue, (new_distance, neighbor))

    if distances[end] == float('inf'):
        return -1, []
    else:
        return distances[end], paths[end]

def solve():
    n, m = map(int, input().split())
    city_owners = list(map(int, input().split()))

    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    cost, path = dijkstra(graph, city_owners, 0, n-1)

    if cost == -1:
        print("impossible")
    else:
        path = [city + 1 for city in path]
        print(cost, len(path))
        print(" ".join(map(str, path)))

solve()
