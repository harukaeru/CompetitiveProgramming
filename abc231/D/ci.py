from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(1000000)
N, M = map(int, input().split())
G = defaultdict(set)
for i in range(M):
  a, b = map(int, input().split())
  G[a].add(b)
  G[b].add(a)


# 頂点数:n
# edge[i]:頂点iと辺で結ばれる頂点の集合

# 遷移元の頂点
parent=[-1]*n
# 閉路に含まれる辺の集合
loop =set()
# 既に探索した頂点か
come=[False]*n

def dfs(x,last=-1):
    if last!=-1:
        parent[x]=last
    come[x]=True
    for i in edge[x]:
        if i ==last:continue
        if come[i]:
            now=x
            loop.add((now,i))
            loop.add((i,now))
            while now!=i:
                loop.add((now,parent[now]))
                loop.add((parent[now],now))
                now=parent[now]
            return True
        else:
            if dfs(i,x):
                return True
    return False

dfs(0)
