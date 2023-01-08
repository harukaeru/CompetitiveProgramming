#!/usr/bin/env pypy3
from collections import defaultdict
import sys
sys.setrecursionlimit(300000)

N,M=map(int, input().split())
G = defaultdict(set)
for i in range(M):
  u,v=map(int, input().split())
  u -= 1
  v -= 1
  G[u].add(v)
  G[v].add(u)

# print(G)

seen = set()
seen.add(0)
cnt = 1

p = 10 ** 6

def dfs(v):
  global cnt
  for nex in G[v]:
    if nex not in seen:
      seen.add(nex)
      cnt += 1
      if cnt > p:
        print(p)
        exit()
      dfs(nex)
      seen.remove(nex)

dfs(0)
print(min(cnt, 10 ** 6))