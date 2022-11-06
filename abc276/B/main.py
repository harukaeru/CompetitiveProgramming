#!/usr/bin/env python3.8
from collections import defaultdict
N, M = map(int, input().split())
G = defaultdict(list)
for i in range(M):
  a, b = map(int, input().split())
  G[a].append(b)
  G[b].append(a)

for v in G.values():
  v.sort()
  v.reverse()

for i in range(1, N + 1):
  G[i].append(len(G[i]))
  G[i].reverse()
  print(*G[i])