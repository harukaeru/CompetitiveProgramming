#!/usr/bin/env pypy3
N = int(input())
A = list(map(int, input().split()))

dp = []
for i in range(1 + N):
  if i == 0:
    d1 = [0, 1e23]
    d2 = [1e23, A[-1]]
  else:
    d1 = [1e23, 1e23]
    d2 = [1e23, 1e23]
  dp.append([d1, d2])

for i in range(N):
  cur = A[i]

  dp[i + 1][True][True] = min(dp[i][True][True] + cur, dp[i][False][True] + cur)
  dp[i + 1][False][True] = dp[i][True][True]

  if i == N - 2:
    dp[i + 1][True][True] = min(dp[i+1][True][True], min(dp[i][True][False] + cur, dp[i][False][False] + cur))
    dp[i + 1][False][False] = min(dp[i + 1][False][False], dp[i][True][False])
    dp[i + 1][True][True] = min(dp[i+1][True][True], dp[i][True][True])
  elif i == N - 1:
    dp[i + 1][True][True] = min(dp[i+1][True][True], dp[i][False][False] + cur)
    dp[i + 1][True][True] = min(dp[i+1][True][True], dp[i][True][True])
  else:
    dp[i + 1][True][False] = min(dp[i][True][False] + cur, dp[i][False][False] + cur)
    dp[i + 1][False][False] = dp[i][True][False]

print(dp[N][True][True])