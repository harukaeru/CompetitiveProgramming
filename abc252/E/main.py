#!/usr/bin/env python3.8
from collections import defaultdict
import heapq

N,M=map(int, input().split())
edges = defaultdict(list)
for i in range(M):
  a,b,c= map(int, input().split())
  a-=1
  b-=1
  edges[a].append((c, b, i))
  edges[b].append((c, a, i))

dists = [1e18] * N
s = 0
dists[s] = 0
pq = [(0, s, None)]

route = [-1] * N
while pq:
  c, v, i = heapq.heappop(pq)
  if dists[v] < c:
    continue
  for edge in edges[v]:
    nc, nv, ni = edge
    candidate = dists[v] + nc
    if dists[nv] > candidate:
      dists[nv] = candidate
      route[nv] = ni
      heapq.heappush(pq, (dists[nv], nv, ni))


route = [r for r in route if r >= 0]
print(*[r + 1 for r in route])