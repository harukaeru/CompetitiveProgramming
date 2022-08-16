#!/usr/bin/env python3
N = int(input())

candidates = [1] + [6 ** i for i in range(1, 7)] + [9 ** i for i in range(1, 6)]

dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, N + 1):
  m = 9999999999
  for candidate in candidates:
    if i >= candidate:
      m = min(m, dp[i - candidate] + 1)
  dp[i] = m

print(dp[N])