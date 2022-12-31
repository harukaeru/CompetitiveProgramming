#!/usr/bin/env python3.8
# https://note.nkmk.me/python-union-find/
from bisect import bisect_left
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

N, M, Q = map(int, input().split())
origs = []
for i in range(M):
  a,b,c=map(int, input().split())
  a-=1
  b-=1
  origs.append((c,a,b))

edges = []
poses = defaultdict(list)
for i in range(Q):
  u,v,w=map(int, input().split())
  u-=1
  v-=1
  edges.append((w,u,v))
  poses[(w,u,v)].append(i)

edges = origs + edges
origs = set(origs)

edges.sort()

uf = UnionFind(N)
anses = [None] * Q
for edge in edges:
  w,u,v = edge
  pos = poses.get(edge, None)
  if pos is not None:
    for p in pos:
      if uf.same(u, v):
        anses[p] = 'No'
      else:
        anses[p] = 'Yes'
    continue
  
  if uf.same(u, v):
    continue
  uf.union(u,v)

for a in anses:
  print(a)