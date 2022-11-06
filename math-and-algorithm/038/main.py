#!/usr/bin/env python3.8
N, Q = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * (N + 1)
for i in range(1, N + 1):
  dp[i] = dp[i - 1] + A[i - 1]

for i in range(Q):
  l, r = map(int, input().split())
  print(dp[r] - dp[l - 1])