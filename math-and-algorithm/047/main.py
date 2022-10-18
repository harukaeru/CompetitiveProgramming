#!/usr/bin/env python3
from collections import defaultdict, deque
N, M = map(int, input().split())
G = defaultdict(list)

for i in range(M):
  a, b = map(int, input().split())
  G[a].append(b)
  G[b].append(a)
  

dists = [-1] * N

for i in range(1, N + 1):
  if dists[i - 1] != -1:
    continue
  dists[i - 1] = 0

  # print('i', i)
  q = deque()
  q.append(i)

  while len(q) > 0:
    v = q.popleft()
    color = dists[v - 1]
    for n in G[v]:
      if dists[n - 1] == -1:
        dists[n - 1] = 1 - color
        q.append(n)
      elif dists[n - 1] == color:
        print('No')
        exit()

if set(dists) == set([0, 1]):
  print('Yes')
else:
  print('No')
