#!/usr/bin/env python3.8
from collections import defaultdict, deque

N,M=map(int, input().split())
G = defaultdict(list)
for i in range(M):
  u,v=map(int, input().split())
  u -= 1
  v -= 1
  G[u].append(v)
  G[v].append(u)

seen = set()
tot = 0
for i in range(N):
  if i in seen:
    continue
  q = deque()
  q.append(i)
  seen.add(i)
  while len(q) > 0:
    v = q.popleft()
    for nex in G[v]:
      if nex not in seen:
        seen.add(nex)
        q.append(nex)
  tot += 1
print(tot)