#!/usr/bin/env python3
N = int(input())

dp = [0, 1, 1, 8]
MOD = 10 ** 9 + 7

for i in range(1, N):
  ac = (dp[0] * 10 + dp[1] + dp[2]) % MOD
  a0 = (dp[1] * 9 + dp[3]) % MOD
  a9 = (dp[2] * 9 + dp[3]) % MOD
  yet = (dp[3] * 8) % MOD
  n_dp = [ac, a0, a9, yet]
  # print(n_dp)
  dp = n_dp

print(dp[0])