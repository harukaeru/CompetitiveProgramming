#!/usr/bin/env python3.8
N,W=map(int, input().split())
dp = []
for i in range(1 + N):
  d = [0] * (1 + W)
  dp.append(d)

for i in range(1, N + 1):
  w, v = map(int, input().split())
  for j in range(W + 1):
    dp[i][j] = max(dp[i][j], dp[i - 1][j])
    if 0 <= j + w <= W:
      dp[i][j + w] = max(dp[i][j + w], dp[i - 1][j] + v)
print(max(dp[N]))