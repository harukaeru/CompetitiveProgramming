#!/usr/bin/env python3.8
# https://note.nkmk.me/python-union-find/
from collections import defaultdict
MOD = 998244353

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
uf = UnionFind(N)
cycles = defaultdict(bool)
for i in range(M):
  u,v=map(int, input().split())
  u-=1
  v-=1
  # print('---')
  # print(uf)
  if uf.same(u, v):
    cycles[u] = True
  uf.union(u, v)

# print(cycles)
# print('roots', uf.roots())
ans = 1
for grp_idx, members in uf.all_group_members().items():
  cnt = 0
  for m in members:
    if cycles[m]:
      cnt += 1
  if cnt == 1:
    ans *= 2
    ans %= MOD
  else:
    ans = 0

print(ans)