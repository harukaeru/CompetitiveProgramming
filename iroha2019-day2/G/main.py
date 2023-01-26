#!/usr/bin/env python3.8
from collections import defaultdict
import heapq

N,M,K=map(int, input().split())
G = defaultdict(list)
for i in range(M):
  a,b,c=map(int, input().split())
  a-=1
  b-=1
  G[a].append((c, b))
  G[b].append((c, a))

X = [None] * N
Y = [None] * N
for i in range(N):
  x,y=map(int, input().split())
  X[i]=x
  Y[i]=y

costs = []
for i in range(K + 1):
  cost = [1e18] * N
  costs.append(cost)

costs[0][0] = 0
pq = [(0, (0, 0))]
if X[0] != 0:
  set_count = ((K + 1) + X[0] - 1) // X[0]
  for count in range(set_count + 1):
    nex_cost = count * Y[0]
    nex_flower = min(count * X[0], K)
    if costs[nex_flower][0] > nex_cost:
      costs[nex_flower][0] = nex_cost
      heapq.heappush(pq, (nex_cost, (nex_flower, 0)))

while len(pq) > 0:
  cost, (flower, v) = heapq.heappop(pq)
  if costs[flower][v] < cost:
    continue
  if K - flower < 0:
    continue
  costs[flower][v] = min(costs[flower][v], cost)

  # for cost in costs:
  #   print([' ' if c == 1e18 else c for c in cost])
  # print('----')

  flower_requirement = K - flower
  for moving_cost, nex in G[v]:
    moving_cost = costs[flower][v] + moving_cost

    if X[nex] == 0:
      costs[flower][nex] = min(costs[flower][nex], moving_cost)
      heapq.heappush(pq, (moving_cost, (flower, nex)))
    else:
      set_count = (flower_requirement + X[nex] - 1) // X[nex]
      for count in range(set_count + 1):
        nex_cost = moving_cost + count * Y[nex]
        nex_flower = min(flower + count * X[nex], K)
        if costs[nex_flower][nex] > nex_cost:
          costs[nex_flower][nex] = nex_cost
          # print(nex_cost, 'count:', count, 'price:', count * Y[nex], (nex_flower, nex))
          heapq.heappush(pq, (nex_cost, (nex_flower, nex)))

ans = costs[K][N - 1]
if ans == 1e18:
  print(-1)
else:
  print(ans)