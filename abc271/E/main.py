#!/usr/bin/env python3.8
from collections import defaultdict
N, M, K = map(int, input().split())

G = defaultdict(list)
dists = {}
ABC = []
for i in range(M):
  a, b, c = map(int, input().split())
  ABC.append((a, b, c))
  G[a].append(b)
E = list(map(int, input().split()))

INF = 1e32

dp = dict()
dp[1] = 0

for k in range(1, K + 1):
  e = E[k - 1] - 1

  a, b, c = ABC[e]
  ma = dp.get(a, INF)

  dist_b = ma + c

  mb = dp.get(b, INF)
  dp[b] = min(mb, dist_b)

d = dp.get(N, INF)
if d == INF:
  print(-1)
else:
  print(d)