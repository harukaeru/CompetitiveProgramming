#!/usr/bin/env python3.8
import heapq


N = int(input())
dp = {}
for i in range(N - 1):
  a, b, c = map(int, input().split())
  a-=1
  b-=1
  dp.setdefault(a, {}).setdefault(b, c)
  dp.setdefault(b, {}).setdefault(a, c)

Q,K=map(int, input().split())
K -= 1

pq = []
pq.append((0, K))
dists = [1e18] * N
dists[K] = 0

while pq:
  d, v = heapq.heappop(pq)
  if dists[v] < d:
    continue

  for nex in dp[v].keys():
    if v == nex:
      continue

    # print('dists[nex]', dists[nex])
    # print('dists[v]', dists[v])
    # print('dists[v] + dp[v][nex]', dists[v] + dp[v][nex])
    if dp.get(v, {}).get(nex) is None:
      continue
    if dists[nex] > dists[v] + dp[v][nex]:
      dists[nex] = dists[v] + dp[v][nex]
      heapq.heappush(pq, (dists[nex], nex))

# for dd in dp.items():
#   print(dd)
# print(dists)
for i in range(Q):
  x,y=map(int, input().split())
  x -= 1
  y -= 1
  print(dists[x] + dists[y])