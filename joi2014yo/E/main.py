#!/usr/bin/env python3.8
from collections import defaultdict
import heapq


N,K=map(int, input().split())
P = []
R = []
for i in range(N):
  p,r = map(int, input().split())
  P.append(p)
  R.append(r)

G = defaultdict(list)
for i in range(K):
  a,b=map(int, input().split())
  a-=1
  b-=1
  G[a].append(b)
  G[b].append(a)


costs = []
for i in range(5001):
  cos = [1e18] * N
  costs.append(cos)

pq = [(P[0], (-R[0], 0))]
for i in range(R[0] + 1):
  costs[i][0] = P[0]

while pq:
  c, (rest, v) = heapq.heappop(pq)
  rest = -rest
  if costs[rest][v] < c:
    continue

  # 降りて乗り継ぐとき。否応なく降りなければならないときもこれ
  for nex in G[v]:
    if nex == N - 1:
      costs[0][nex] = min(costs[0][nex], c)
      continue

    next_cost = c + P[nex]
    if costs[0][nex] > next_cost:
      costs[0][nex] = next_cost
      heapq.heappush(pq, (next_cost, (-R[nex], nex)))

  # 降りずにそのまま乗車するとき
  if rest > 1:
    for nex in G[v]:
      next_cost = c
      if costs[rest - 1][nex] > next_cost:
        costs[rest - 1][nex] = next_cost
        heapq.heappush(pq, (next_cost, (-(rest - 1), nex)))

md = 1e18
for c in costs:
  md = min(md, c[N - 1])
print(md)