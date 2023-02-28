#!/usr/bin/env pypy3
from collections import defaultdict


N,M=map(int, input().split())
G = defaultdict(set)
F = defaultdict(set)
for i in range(M):
  x,y=map(int, input().split())
  x -= 1
  y -= 1
  G[x].add(y)
  F[y].add(x)


dp = [0] * (2 ** N)
dp[0] = 1
for i in range(0, 2 ** N):
  s = i
  for j in range(N):
    if i & (1 << j):
      continue
    ok = True
    for k in range(N):
      if (s & (1 << k) != 0) and j in G[k]:
        ok = False
    if ok:
      dp[s | (1 << j)] += dp[i]


print(dp[(1 << N) - 1])