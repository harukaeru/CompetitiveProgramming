#!/usr/bin/env python3.8
MOD = 998244353
N, M, K = map(int, input().split())

dp = []

for i in range(N + 1):
  dp.append([0] * (K + 1))

dp[0][0] = 1
for i in range(1, N + 1):
  cums = [0] * (len(dp[i]) + 1)
  for di0, d in enumerate(dp[i - 1]):
    cums[di0 + 1] = cums[di0] + d

  for di, d in enumerate(dp[i]):
    L = max(di - M, 0)
    dp[i][di] = cums[di] - cums[L]
    # for m in range(1, M + 1):
    #   if di + m <= K:
    #     dp[i][di + m] += (dp[i - 1][di] % MOD)

  # print(dp[i])

print(sum(dp[N]) % MOD)