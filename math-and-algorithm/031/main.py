#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

dp = [None] * (N + 1)
dp[0] = 0
dp[1] = A[0]

for i in range(2, N + 1):
  a = A[i - 1]
  dp[i] = max(dp[i - 2] + a, dp[i - 1])
print(dp[N])