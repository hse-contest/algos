class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, a, b):
        self.graph[a].append(b)

    def find_cycle(self):
        state = [0] * self.n
        parent = [-1] * self.n
        cycle_end = -1
        cycle_start = -1

        def dfs(v):
            nonlocal cycle_start, cycle_end
            state[v] = 1

            for neighbor in self.graph[v]:
                if state[neighbor] == 0:
                    parent[neighbor] = v
                    if dfs(neighbor):
                        return True
                elif state[neighbor] == 1:
                    cycle_end = v
                    cycle_start = neighbor
                    return True

            state[v] = 2
            return False

        for i in range(self.n):
            if state[i] == 0 and dfs(i):
                cycle = []
                current = cycle_end
                while current != cycle_start:
                    cycle.append(current)
                    current = parent[current]
                cycle.append(cycle_start)
                cycle.reverse()
                return cycle

        return None

def main():
    n, m = map(int, input().split())
    graph = Graph(n)

    for _ in range(m):
        a, b = map(lambda el: int(el) - 1, input().split())
        graph.add_edge(a, b)

    cycle = graph.find_cycle()

    if not cycle:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(lambda el: str(el + 1), cycle)))

if __name__ == "__main__":
    main()
