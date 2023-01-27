#!/usr/bin/env python3.8
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

N = int(input())
XY = []
for i in range(N):
  x,y=map(int, input().split())
  x-=1
  y-=1
  XY.append((x, y, i))

XY_BY_X = list(sorted(XY, key=lambda a: a[0]))
XY_BY_Y = list(sorted(XY, key=lambda a: a[1]))

edges = []
for i in range(N - 1):
  dx = abs(XY_BY_X[i][0] - XY_BY_X[i + 1][0])
  dy = abs(XY_BY_X[i][1] - XY_BY_X[i + 1][1])
  d = min(dx, dy)
  edges.append((d, (XY_BY_X[i][2], XY_BY_X[i + 1][2])))

for i in range(N - 1):
  dx = abs(XY_BY_Y[i][0] - XY_BY_Y[i + 1][0])
  dy = abs(XY_BY_Y[i][1] - XY_BY_Y[i + 1][1])
  d = min(dx, dy)
  edges.append((d, (XY_BY_Y[i][2], XY_BY_Y[i + 1][2])))

edges.sort()

uf = UnionFind(N)
total = 0
for e in edges:
  cost, (x, y) = e
  if uf.same(x, y):
    continue
  total += cost
  uf.union(x, y)
print(total)
