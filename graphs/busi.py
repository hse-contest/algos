import sys
sys.setrecursionlimit(10**7)

n = int(input())

graph = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, visited=set(), from_node=-1):
    visited.add(node)
    max_depth = 1
    for neighbor in graph[node]:
        if neighbor != from_node:
            max_depth = max(dfs(neighbor, visited, node) + 1, max_depth)
    return max_depth

print(max(dfs(i) for i in range(n)))
