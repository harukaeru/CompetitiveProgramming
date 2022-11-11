#!/usr/bin/env python3.8
from collections import defaultdict
N, M = map(int, input().split())
G = defaultdict(int)
for i in range(M):
  a, b = map(int, input().split())
  G[a] += 1
  G[b] += 1

for i in range(1, N + 1):
  print(G[i])