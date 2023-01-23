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

def dijkstra(start):
  p_queue = [(0, start)]

  dists = [1e18] * N
  dists[start] = 0

  while len(p_queue) > 0:
    d, current_node = heapq.heappop(p_queue)
    # 別になくても動くけど、priority_queueに同一nodeが何個も入ることがあるので、
    # 同じのが入ったときにわざわざfor文に行きたくない。そのためここでちょんぎっている
    if dists[current_node] < d:
      continue

    for d_from_current_to_nex, nex_node in G[current_node]:
      d_from_start_to_nex = d_from_current_to_nex + dists[current_node]
      if dists[nex_node] > d_from_start_to_nex:
        dists[nex_node] = d_from_start_to_nex
        heapq.heappush(p_queue, (d_from_start_to_nex, nex_node))
  return dists

md = 1e18
for i in range(N):
  costs = dijkstra(i)
  md = min(md, max(costs))
print(md)
