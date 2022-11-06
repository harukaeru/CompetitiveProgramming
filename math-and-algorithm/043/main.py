#!/usr/bin/env python3.8
from collections import defaultdict
N, M = map(int, input().split())
G = defaultdict(list)

for i in range(M):
  a, b = map(int, input().split())
  G[a].append(b)
  G[b].append(a)

seen = set()
q = []
q.append(1)
seen.add(1)

while len(q) > 0:
  v = q.pop()
  for nex in G[v]:
    if nex not in seen:
      seen.add(nex)
      q.append(nex)
  
if len(seen) != N:
  print('The graph is not connected.')
else:
  print('The graph is connected.')
