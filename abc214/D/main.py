#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

N = int(input())

edges = []

for i in range(N - 1):
    *x, = map(int, input().split())
    u_i, v_i, w_i = x
    u_i -= 1
    v_i -= 1
    edges.append([w_i, (u_i, v_i)])

edges.sort(key=lambda e: e[0])

class UnionFind:
    def __init__(self, values):
        self.parent = {}
        for v in values:
            self.parent[v] = -1

    def find(self, x):
        if self.parent[x] <= -1:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return

        self.parent[px] += self.parent[py]
        self.parent[py] = x

    def size(self, x):
        return -self.parent[self.find(x)]

uf = UnionFind(list(range(N)))

ans = 0
for edge in edges:
    w, (u, v) = edge
    ans += w * uf.size(u) * uf.size(v)
    uf.unite(u, v)
print(ans)
