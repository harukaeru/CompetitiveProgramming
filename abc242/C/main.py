#!/usr/bin/env python3
N = int(input())

MOD = 998244353
dp = [1] * 9

for n in range(N - 1):
  new_dp = [0] * 9
  for i in range(9):
    prev = dp[i - 1] if i - 1 >= 0 else 0
    nex = dp[i + 1] if i + 1 < 9 else 0
    new_dp[i] += prev % MOD + dp[i] + nex % MOD
  dp = new_dp

print(sum(new_dp) % MOD)