class Tree:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.n = n

    def find(self, el):
        if self.parent[el] == el:
            return el
        return self.find(self.parent[el])

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)

        if pa == pb:
            return False

        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        elif self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1

        return True

    def is_simple(self):
        family = {}
        for i in range(self.n):
            p = self.find(i)
            if p not in family:
                family[p] = len(family) + 1

        return len(family) == 1


def is_console_tree():
    n, m = map(int, input().split())
    tree = Tree(n)
    for _ in range(m):
        a, b = map(lambda el: int(el) - 1, input().split())
        if not tree.union(a, b):
            return False
    return tree.is_simple()

print("YES" if is_console_tree() else "NO")
