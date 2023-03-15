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


N,M=map(int, input().split())

edges = []
for i in range(N):
  edges.append((i, i + N))

for i in range(M):
  a,b,c,d=input().split()
  a = int(a)
  c = int(c)
  a -= 1
  c -= 1
  if b == 'B':
    a += N
  if d == 'B':
    c += N
  edges.append((a, c))

uf = UnionFind(2 * N)
cnt = 0
for edge in edges:
  if uf.same(edge[0], edge[1]):
    cnt += 1
  uf.union(edge[0], edge[1])

# print(cnt)
# print(uf.all_group_members())
print(cnt, uf.group_count() - cnt)