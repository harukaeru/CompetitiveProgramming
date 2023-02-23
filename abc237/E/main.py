#!/usr/bin/env python3.8
from collections import defaultdict, deque
import heapq


N,M=map(int, input().split())
H = list(map(int, input().split()))

G = {}
for i in range(M):
  u,v=map(int, input().split())
  u -= 1
  v -= 1
  if H[u] <= H[v]:
    v,u = u,v

  d = H[u] - H[v]
  G.setdefault(u, {}).setdefault(v, 0)
  G.setdefault(v, {}).setdefault(u, d)

# print(G)
dists = [1e18] * N
dists[0] = 0

pq = []
pq.append((0, 0))
while pq:
  score, u = heapq.heappop(pq)
  if dists[u] > score:
    continue

  for v, v_cost in G.get(u, {}).items():
    if dists[u] + v_cost < dists[v]:
      dists[v] = dists[u] + v_cost
      heapq.heappush(pq, (dists[v], v))

# print(dists)
ans = 0
for i in range(N):
  ans = min(ans, dists[i] - (H[0] - H[i]))
# print(dists)
print(-ans)