#!/usr/bin/env python3.8
import sys
sys.setrecursionlimit(300000)

import heapq
from collections import defaultdict
N, M = map(int, input().split())

D = defaultdict(list)
G = defaultdict(int)

for i in range(M):
  a, b = map(int, input().split())
  D[a].append(b)
  G[b] += 1

values = []

glist = []
for i in range(1, N + 1):
  if G[i] == 0:
    glist.append(i)
heapq.heapify(glist)

while len(values) < N:
  if len(glist) == 0:
    print(-1)
    exit()
  v = heapq.heappop(glist)
  values.append(v)

  for nex in D[v]:
    G[nex] -= 1
    if G[nex] == 0:
      heapq.heappush(glist, nex)

print(*values)
