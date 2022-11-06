#!/usr/bin/env python3.8
from collections import defaultdict
V, E = map(int, input().split())

if E == 0:
  print(-1)
  exit()

G = defaultdict(dict)
for i in range(E):
  s, t, d = map(int, input().split())
  G[s][t] = d

INF = 9999999999

dp = []
for i in range(32800):
  d = [INF] * 20
  dp.append(d)

dp[0][0] = 0

for s in range(1 << V):
  for u in range(V):
    for v in range(V):
      if s != 0 and not (s & (1 << u)):
        continue
      if s & (1 << v) == 0:
        if v != u:
          dp[s | (1 << v)][v] = min(dp[s | (1 << v)][v], dp[s][u] + G[u].get(v, INF))

# for i, d in enumerate(dp):
#   x = '{:020b}'.format(i)
#   print([19 - i for i, b in enumerate(x) if b == '1'])
ans = dp[(1 << V) - 1][0]
if ans == INF:
  print(-1)
else:
  print(ans)