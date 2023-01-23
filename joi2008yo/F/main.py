#!/usr/bin/env pypy3
import heapq


N,K=map(int, input().split())

G = []
for i in range(N):
  g = []
  for j in range(N):
    if i == j:
      g.append(0)
    else:
      g.append(1e18)
  G.append(g)

def dijkstra(s):
  pq = [(0, s)]
  dists = [1e18] * N
  dists[s] = 0
  while pq:
    d, v = heapq.heappop(pq)
    if dists[v] < d:
      continue

    for nex in range(N):
      dd = G[v][nex]
      if dists[nex] > dists[v] + dd:
        dists[nex] = dists[v] + dd
        heapq.heappush(pq, (dists[nex], nex))
  return dists

for i in range(K):
  q, *x = map(int, input().split())
  if q == 0:
    a,b = x
    a -= 1
    b -= 1
    ans = dijkstra(a)[b]
    
    if ans == 1e18:
      print(-1)
    else:
      print(ans)
  else:
    c,d,e=x
    c -= 1
    d -= 1
    G[c][d] = min(G[c][d], e)
    G[d][c] = min(G[d][c], e)