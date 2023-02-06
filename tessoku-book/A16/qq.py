#!/usr/bin/env python3.8
N = int(input())
A = [1e18, 1e18] + list(map(int, input().split()))
B = [1e18, 1e18, 1e18] + list(map(int, input().split()))

dp = [1e18] * (N + 1)
dp[1] = 0

for i in range(1, N):
  dp[i + 1] = min(dp[i + 1], dp[i] + A[i + 1])
  if i + 2 <= N:
    dp[i + 2] = min(dp[i + 2], dp[i] + B[i + 2])

print(dp[N])