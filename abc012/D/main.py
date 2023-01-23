#!/usr/bin/env python3.8
from collections import defaultdict
import heapq

N,M= map(int, input().split())

G = defaultdict(list)
for i in range(M):
  a,b,t=map(int, input().split())
  a -= 1
  b -= 1
  G[a].append((t, b))
  G[b].append((t, a))

def dijkstra(s):
  pq = [(0, s)]
  costs = [1e18] * N
  costs[s] = 0

  while len(pq) > 0:
    c, pos = heapq.heappop(pq)
    if costs[pos] < c:
      continue
    
    for nex_cost, nex in G[pos]:
      cand = nex_cost + costs[pos]
      if costs[nex] > cand:
        costs[nex] = cand
        heapq.heappush(pq, (cand, nex))
  return costs

md = 1e18
for i in range(N):
  costs = dijkstra(i)
  md = min(md, max(costs))
print(md)
