#!/usr/bin/env python3.8
V, E = map(int, input().split())
dists = []
for i in range(V):
  d = [1e18] * V
  dists.append(d)

for i in range(E):
  s,t,d=map(int, input().split())
  dists[s][t] = d

dp = []
for i in range(2 ** V):
  d = [1e18] * V
  dp.append(d)

K = 0
for v in range(V):
  dp[0][K] = 0

for i in range(2 ** V):
  for j in range(V):
    for k in range(V):
      # if ((i >> k) & 1) == 0:
      print(f'dp[{i}][{j}] + dists[{j}][{k}])', dp[i][j] + dists[j][k])
      dp[i | (1 << k)][k] = min(dp[i | (1 << k)][k], dp[i][j] + dists[j][k])

for i, d in enumerate(dp):
  print(bin(i), d)

ans = dp[2 ** V - 1][K]
if ans == 1e18:
  print(-1)
else:
  print(ans)