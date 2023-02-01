#!/usr/bin/env python3.8
N,W=map(int, input().split())
items = []
V = 0
for i in range(N):
  w,v=map(int, input().split())
  items.append((w,v))
  V += v

dp = []
for i in range(N+1):
  d = [1e18] * (1+V)
  dp.append(d)

dp[0][0] = 0

for i in range(1,N+1):
  w,v = items[i - 1]
  for j in range(1+V):
    dp[i][j] = min(dp[i][j], dp[i-1][j])
    if dp[i-1][j] + w <= W:
      dp[i][j + v] = min(dp[i][j+v], dp[i-1][j] + w)

# for d in dp:
#   print(d)

mi = i
for i, d in enumerate(dp[N]):
  if d == 1e18:
    continue
  mi = max(mi, i)

print(mi)