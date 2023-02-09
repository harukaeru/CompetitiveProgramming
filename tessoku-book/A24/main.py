#!/usr/bin/env python3.8
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
X = 500000

L = [1e18] * (X)
dp = [0] * (1 + X)

for i in range(N):
  idx = bisect_left(L, A[i])

  L[idx] = min(L[idx], A[i])
  dp[A[i]] = idx + 1

# print(dp)
print(max(dp))