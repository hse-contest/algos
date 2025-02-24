n, m, k = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, c))

l = int(input())
program = list(map(int, input().split()))

s = int(input()) - 1

nodes = [s]
is_gavno = False
for color in program:
    new_nodes = []
    for node in nodes:
        is_gavno = True
        for next_node, next_color in graph[node]:
            if next_color == color:
                new_nodes.append(next_node)
                is_gavno = False
        if is_gavno:
            break;
    if is_gavno:
        break
    nodes = new_nodes

if is_gavno:
    print("Hangs")
else:
    print("OK")
    print(len(nodes))
    print(" ".join(map(str,sorted(nodes))))
