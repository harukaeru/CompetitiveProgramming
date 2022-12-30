#!/usr/bin/env python3.8
# https://note.nkmk.me/python-union-find/
from collections import Counter, defaultdict

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
N, M, K = map(int, input().split())
friends = UnionFind(N)
f_counter = Counter()
for i in range(M):
  a,b = map(int, input().split())
  a-=1
  b-=1
  friends.union(a,b)
  f_counter[a] += 1
  f_counter[b] += 1

blocks = UnionFind(N)
b_counter = Counter()
for i in range(K):
  c,d = map(int, input().split())
  c-=1
  d-=1
  if friends.same(c, d):
    b_counter[c] += 1
    b_counter[d] += 1

anses = []
for i in range(N):
  r = friends.find(i)
  size = friends.size(r)
  ans = size - f_counter[i] - b_counter[i] - 1
  anses.append(ans)
print(*anses)

