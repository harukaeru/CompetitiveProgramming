#!/usr/bin/env python3
from collections import defaultdict
N, K, L = map(int, input().split())


class UnionFind:
    def __init__(self, values):
        self.parent = [-1] * len(values)

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
        self.parent[py] = px

    def size(self, x):
        return -self.find(x)



n = list(range(N))
k_uf = UnionFind(n)

for __ in range(K):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    k_uf.unite(p, q)

l_uf = UnionFind(n)
for __ in range(L):
    r, s = map(int, input().split())
    r -= 1
    s -= 1
    l_uf.unite(r, s)

groups_counter = defaultdict(int)

# 各都市のグループ同士をマッピング
for i in range(N):
    pk = k_uf.find(i)
    pl = l_uf.find(i)
    groups_counter[(pk, pl)] += 1

ans = []
for i in range(N):
    pk = k_uf.find(i)
    pl = l_uf.find(i)
    ans.append(groups_counter[(pk, pl)])

print(*ans)
