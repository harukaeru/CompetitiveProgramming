#!/usr/bin/env python3
MOD = 998244353
N, M, K = map(int, input().split())

dp = []

for i in range(N + 1):
  dp.append([0] * (K + 1))

dp[0][0] = 1
for i in range(1, N + 1):
  for di, d in enumerate(dp[i]):
    for m in range(1, M + 1):
      if di + m <= K:
        dp[i][di + m] += (dp[i - 1][di] % MOD)

print(sum(dp[N]) % MOD)