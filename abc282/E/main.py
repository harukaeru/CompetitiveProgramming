#!/usr/bin/env pypy3
# https://note.nkmk.me/python-union-find/
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
N, M = map(int, input().split())
A = list(map(int, input().split()))

pairs = {}
for i in range(N - 1):
  for j in range(i + 1, N):
    l = A[i]
    r = A[j]
    pairs[(i, j)] = (pow(l, r, M) + pow(r, l, M)) % M

# print(pairs)

uf = UnionFind(N)

edges = []

for k, v in pairs.items():
    edges.append((-v, k[0], k[1]))

# 重みが小さい順に辺をソート
edges.sort()

cost = 0

for edge in edges:
    c, u, v = edge
    # 頂点がつながっていなければ
    if not uf.same(u, v):
        cost += c # 重みを足し
        uf.union(u, v) # 頂点同士をつなげる

print(-cost)