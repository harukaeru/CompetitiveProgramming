#!/usr/bin/env python3.8
N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [None] * (N + 1)
dp[0] = 0

for n in range(1, N + 1):
  max_d = 0
  for j in range(K):
    if n >= A[j]:
      max_d = max(max_d, n - dp[n - A[j]])
  dp[n] = max_d

print(dp[N])