#!/usr/bin/env python3
N, M = map(int, input().split())
X = list(map(int, input().split()))
bonus = {}
for i in range(M):
  c, y = map(int, input().split())
  bonus[c] = y

dp = []
for i in range(N + 1):
  d = [None] * (N + 1)
  dp.append(d)
dp[0][0] = 0

for i in range(1, N + 1):
  x = X[i - 1]
  dp[i][0] = max([d for d in dp[i - 1] if d is not None])
  for j in range(N):
    if dp[i - 1][j] is not None:
      dp[i][j + 1] = dp[i - 1][j] + x + bonus.get(j + 1, 0)
      if dp[i - 1][j + 1] is not None:
        dp[i][j + 1] = max(dp[i][j + 1], dp[i - 1][j + 1])

print(max(dp[N]))