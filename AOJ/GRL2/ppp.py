V, E = map(int, input().split())
G = {}
edge_costs = {}
for i in range(V):
    G[i] = []

for i in range(E):
    s, t, w = map(int, input().split())
    G[s].append(t)
    G[t].append(s)
    if not edge_costs.get(w):
        edge_costs[w] = []
    edge_costs[w].append((s, t))

class UnionFind:
    def __init__(self, values):
        self.parent = {}
        for v in values:
            self.parent[v] = -1

    def find(self, x):
        if self.parent[x] == -1:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        self.parent[px] = py

uf = UnionFind(list(range(V)))
ans = 0
for key in sorted(edge_costs):
    for s, t in edge_costs[key]:
        if uf.find(s) == uf.find(t):
            continue
        ans += key
        uf.unite(s, t)
print(ans)
