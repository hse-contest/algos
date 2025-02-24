# DSU
n, m = map(int, input().split())

parent = list(range(n))
rank = [0] * n

def find(el):
    if parent[el] == el:
        return el
    return find(parent[el])

def union(a, b):
    pa, pb = find(a), find(b)

    if pa == pb:
        return

    if rank[pa] < rank[pb]:
        parent[pa] = pb
    elif rank[pa] > rank[pb]:
        parent[pb] = pa
    else:
        parent[pb] = pa
        rank[pa] += 1

for _ in range(m):
    a, b = map(lambda el: int(el) - 1, input().split())
    union(a, b)

family = {}
res = ""
for i in range(n):
    p = find(i)
    if p not in family:
        family[p] = len(family) + 1
    res += str(family[p]) + " "


print(len(family))
print(res)
