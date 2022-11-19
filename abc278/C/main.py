#!/usr/bin/env python3.8
from collections import defaultdict


N, Q = map(int, input().split())
G = defaultdict(set)
for i in range(Q):
  t, a, b = map(int, input().split())
  if t == 1:
    G[a].add(b)
  if t == 2:
    if b in G[a]:
      G[a].remove(b)
  if t == 3:
    if b in G[a] and a in G[b]:
      print('Yes')
    else:
      print('No')
