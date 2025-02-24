def solve():
    n, m, k = map(int, input().split())

    graph = {}

    for _ in range(m):
        u, v, c = map(int, input().split())
        if u not in graph:
            graph[u] = {}
        if c not in graph[u]:
            graph[u][c] = []
        graph[u][c].append(v)

    l = int(input())
    program = list(map(int, input().split()))

    start = int(input())

    rooms = {start}
    for color in program:
        next_rooms = set()
        for room in rooms:
            if room in graph and color in graph[room]:
                for next_room in graph[room][color]:
                    next_rooms.add(next_room)
        if not next_rooms:
            print("Hangs")
            return
        rooms = next_rooms

    res = sorted(list(rooms))

    print("OK")
    print(len(res))
    print(" ".join(map(str, res)))

solve()
