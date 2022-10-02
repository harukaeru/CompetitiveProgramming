#!/usr/bin/env pypy3
N, W = map(int, input().split())
weights = []
values = []
for i in range(N):
  w, v = map(int, input().split())
  weights.append(w)
  values.append(v)

mmm = -9999999999
dp = []
for i in range(N + 1):
  d = [mmm] * (W + 1)
  dp.append(d)
dp[0][0] = 0

for i in range(1, N + 1):
  current_w = weights[i - 1]
  current_v = values[i - 1]
  for w in range(W + 1):
    if w - current_w < 0:
      dp[i][w] = dp[i - 1][w]
    else:
      dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - current_w] + current_v)

print(max(dp[N]))