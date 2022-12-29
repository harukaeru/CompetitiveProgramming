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
  u -= 1
  v -= 1
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

uf = UnionFind(N + M)
for k, v in G.items():
  for vv in v:
    uf.union(k, vv)

eles = {}
cities = {}
for k, members in uf.all_group_members().items():
  e = False
  c = 0
  for m in members:
    if m >= N:
      e = True
    else:
      c += 1
  eles[k] = e
  cities[k] = c

anses = []
ans = 0
for i in range(N):
  p = uf.find(i)
  ans += eles[p]
anses.append(ans)

for i in range(Q - 1):
  x = X[Q - i - 1]
  u,v = edges[x]
  pu = uf.find(u)
  pv = uf.find(v)
  eu = eles[pu]
  ev = eles[pv]
  if not eu and not ev:
    anses.append(ans)
  elif eu and ev:
    anses.append(ans)
  elif eu:
    ans += cities[pv]
    anses.append(ans)
    eles[pv] = True
  else:
    ans += cities[pu]
    anses.append(ans)
    eles[pu] = True
  if uf.same(u, v):
    continue
  uf.union(u, v)
  pvv = cities.get(pv)
  puu = cities.get(pu)
  cities[pv] += puu
  cities[pu] += pvv

anses.reverse()
for a in anses:
  print(a)