import sys
sys.setrecursionlimit(10**7)

def dfs(a, graph, state, parent, cycle_start, cycle_end):
    state[a] = 1

    for b in graph[a]:
        if state[b] == 0:
            parent[b] = a
            if dfs(b, graph, state, parent, cycle_start, cycle_end):
                return True
        elif state[b] == 1:
            cycle_end[0] = a
            cycle_start[0] = b
            return True

    state[a] = 2
    return False

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

state = [0] * (n+1)
parent = [-1] * (n+1)

cycle_start = [-1]
cycle_end = [-1]

for v in range(1, n+1):
    if state[v] == 0 and dfs(v, graph, state, parent, cycle_start, cycle_end):
        break

if cycle_start[0] == -1:
    print("NO")
else:
    print("YES")

    cycle = []
    cycle.append(cycle_start[0])

    v = cycle_end[0]
    while v != cycle_start[0]:
        cycle.append(v)
        v = parent[v]

    print(" ".join(map(str, cycle[::-1])))
