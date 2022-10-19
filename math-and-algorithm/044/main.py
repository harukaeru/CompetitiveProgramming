#!/usr/bin/env python3
from collections import defaultdict, deque
N, M = map(int, input().split())
G = defaultdict(list)
for i in range(M):
  a, b = map(int, input().split())
  G[a].append(b)
  G[b].append(a)

q = deque()
q.append(1)
dists = [-1] * N
dists[0] = 0

while len(q) > 0:
  v = q.popleft()
  for nex in G[v]:
    if dists[nex - 1] == -1:
      dists[nex - 1] = dists[v - 1] + 1
      q.append(nex)

for i in range(N):
  print(dists[i])
