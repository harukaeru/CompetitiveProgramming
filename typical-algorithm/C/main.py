#!/usr/bin/env python3.8
N = int(input())
A = []
for i in range(N):
  X = list(map(int, input().split()))
  A.append(X)

dp = []
for i in range(2 ** N):
  d = [1e18] * N
  dp.append(d)

dp[0][0] = 0

for i in range(2 ** N):
  for j in range(N):
    for k in range(N):
      if ((i >> k) & 1) == 0:
        dp[i | (1 << k)][k] = min(dp[i | (1 << k)][k], dp[i][j] + A[j][k])

# for i, d in enumerate(dp):
#   print(bin(i), d)

print(dp[2 ** N - 1][0])