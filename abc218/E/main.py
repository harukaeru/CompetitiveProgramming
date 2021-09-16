#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

class UnionFind:
    def __init__(self, length):
        self.parent = [-1] * length

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

        self.parent[py] = x

N, M = map(int, input().split())
uf = UnionFind(N)
edges = []

for i in range(M):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1

    edges.append(((a, b), c))

    # oc = edges.get((a, b))
    # if oc is None:
    #     edges[(a, b)] = c
    # elif oc > c:
    #     edges[(a, b)] = c

edges = list(sorted(edges, key=lambda x: x[1]))

total = 0
# print('edge', edges)
for (a, b), c in edges:
    # print('a,b', a, b, '=>', c)
    pa = uf.find(a)
    pb = uf.find(b)
    if pa == pb:
        # print('SAME: a,b', a, b, '=>', c)
        if c >= 0:
            total += c
        continue

    uf.unite(a, b)
    # print('a,b(', a, b, ') =', c)
print(total)
