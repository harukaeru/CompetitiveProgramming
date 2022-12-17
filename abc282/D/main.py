#!/usr/bin/env pypy3
# https://note.nkmk.me/python-union-find/
from collections import defaultdict, deque
from itertools import groupby

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
uf = UnionFind(N * 2)
edges = set()
G = defaultdict(list)
for i in range(M):
  u, v = map(int, input().split())
  edges.add((u, v))
  u -= 1
  v -= 1
  uf.union(u, v + N)
  uf.union(u + N, v)
  G[u].append(v)
  G[v].append(u)

d = defaultdict(list)
for gk, gs in uf.all_group_members().items():
  ngs = [g + 1 for g in gs if g < N]
  # if not ngs:
  #   continue
  d[gk] = ngs
  # if gk >= N:
  #   d[gk % N] += ngs
  #   del d[gk]

le = len(d.items())
if not (le <= 1 or le >= 3):
  k = list(d.values())
  tot = len(k[0]) * len(k[1])
  # print(tot - M)
  print(tot - len(edges))
  exit()

colors = [1e18] * N
c = 1
for i in range(N):
  if colors[i] == 1e18:
    colors[i] = c
    c += 1
  q = deque()
  q.append(i)
  while len(q) > 0:
    vv = q.popleft()
    for nex in G[vv]:
      if colors[nex] == 1e18:
        colors[nex] = colors[i]
        q.append(nex)


ll = list(groupby(sorted(colors)))
if len(ll) > 3 or len(ll) < 1:
  print(0)
  exit()

a = len(list(ll[0][1]))
b = len(list(ll[1][1]))
print(a * b)
exit()

