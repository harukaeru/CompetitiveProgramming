N = 100

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

    def unite(self, x, y):
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
# par = [-1]*(N+1)
# def find(x):
#     if par[x] < 0:
#         return x
#     else:
#         par[x] = find(par[x]) #経路圧縮
#         return par[x]
# def same(x,y):
#     return find(x) == find(y)
# def unite(x,y):
#     x = find(x)
#     y = find(y)
#     if x == y:
#         return 0
#     else:
#       if par[x] > par[y]:
#         x,y = y,x
#         par[x] += par[y]
#         par[y] = x
# def size(x):
#     return -par[find(x)]


uf = UnionFind(N)
uf.unite(1, 2)
uf.unite(2, 3)
uf.unite(1, 4)
uf.unite(2, 5)
uf.unite(5, 6)

print(uf.size(5))
