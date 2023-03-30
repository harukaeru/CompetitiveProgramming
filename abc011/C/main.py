#!/usr/bin/env python3.8
N = int(input())
NG1 = int(input())
NG2 = int(input())
NG3 = int(input())

if N == NG1 or N == NG2 or N == NG3:
  print('NO')
  exit()

ngs = set([NG1, NG2, NG3])
dp = [1e18] * (N + 1)
dp[N] = 0
for i in range(N, -1, -1):
  if i - 1 >= 0 and i - 1 not in ngs:
    dp[i - 1] = min(dp[i - 1], dp[i] + 1)

  if i - 2 >= 0 and i - 2 not in ngs:
    dp[i - 2] = min(dp[i - 2], dp[i] + 1)

  if i - 3 >= 0 and i - 3 not in ngs:
    dp[i - 3] = min(dp[i - 3], dp[i] + 1)

if dp[0] <= 100:
  print('YES')
else:
  print('NO')