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

N, M, E = map(int, input().split())

G = defaultdict(set)
edges = []
for i in range(E):
  u,v = list(map(int, input().split()))
  G[u].add(v)
  G[v].add(u)
  edges.append((u, v))

Q = int(input())
X = []
for i in range(Q):
  x = int(input())
  x -= 1
  X.append(x)

for x in X:
  u,v = edges[x]
  G[u].remove(v)
  G[v].remove(u)

uf = UnionFind()
for k, v in G.items():
  uf.union(k, v)


anses = []
for i in range(Q):
  x = X[i]
  u,v = edges[x]
  G[u].add(v)
  G[v].add(u)