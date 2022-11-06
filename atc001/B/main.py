#!/usr/bin/env python3.8
N, Q = map(int, input().split())

class UnionFind:
    def __init__(self, values):
        self.parent = {}
        for v in values:
            self.parent[v] = -1

    def find(self, v):
        if self.parent[v] == -1:
            return v
        else:
            self.parent[v] = self.find(self.parent[v])
            return self.parent[v]

    def unite(self, x, y):
        p = self.find(x)
        q = self.find(y)
        if p != q:
            self.parent[x] = y

vals = list(range(N))
uf = UnionFind(vals)

for __ in range(Q):
    P, A, B = map(int, input().split())
    if P == 0:
        uf.unite(A, B)
    else:
        if uf.find(B) == uf.find(A):
            print('Yes')
        else:
            print('No')
