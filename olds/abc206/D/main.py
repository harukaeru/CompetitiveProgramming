#!/usr/bin/env python3.8
import sys
sys.setrecursionlimit(300000)

N = int(input())
*a, = map(int, input().split())

mid = N // 2
left = a[:mid]
right = a[mid:]
right.reverse()
edges = []
for i in range(len(left)):
    edges.append((left[i], right[i]))
# edges = list((zip(left, right)))

class UnionFind:
    def __init__(self, length):
        self.parent = [-1] * length

    def find(self, a):
        pa = self.parent[a]
        if pa == -1:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def unite(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        self.parent[pb] = a

uf = UnionFind(200001)
count = 0
edges.sort()
for edge in edges:
    if edge[0] == edge[1]:
        continue
    edge = edge[0] - 1, edge[1] - 1

    x = uf.find(edge[0])
    y = uf.find(edge[1])
    if  x != y:
        uf.unite(edge[0], edge[1])
        count += 1
        continue

# print(left)
# print(right)
print(count)
