#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [-1e18] * (N)
dp[0] = 0

for i in range(N - 1):
  a = A[i]
  b = B[i]
  a -= 1
  b -= 1
  dp[a] = max(dp[a], dp[i] + 100)
  dp[b] = max(dp[b], dp[i] + 150)

# print(dp)
print(dp[N-1])