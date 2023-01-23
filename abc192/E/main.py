#!/usr/bin/env python3.8
from collections import defaultdict
from email.policy import default
import heapq


N,M,X,Y=map(int, input().split())
X-=1
Y-=1

K = defaultdict(dict)
T = defaultdict(dict)
for i in range(M):
  a,b,t,k=map(int, input().split())
  a-=1
  b-=1
  K[a].setdefault(b, []).append(k)
  K[b].setdefault(a, []).append(k)
  T[a].setdefault(b, []).append(t)
  T[b].setdefault(a, []).append(t)

pq = [(0, X)]
dists = [1e18] * N
dists[X] = 0
while pq:
  d, v = heapq.heappop(pq)
  if dists[v] < d:
    continue

  for nex, ts in T[v].items():
    for j,t in enumerate(ts):
      if t == 1e18:
        continue
      # if dists[v] == 1e18:
      #   continue

      # print('dists[v]', dists[v])
      k = K[v][nex][j]
      w = dists[v] if dists[v] % k == 0 else dists[v] // k * k + k
      # print(v+1, '->', nex+1, 'w:', w, 't:', t, 'cost:', w+t)
      new_cost = w + t
      if dists[nex] > new_cost:
        dists[nex] = new_cost
        heapq.heappush(pq, (new_cost, nex))

ans = dists[Y]
if ans == 1e18:
  print(-1)
else:
  print(ans)