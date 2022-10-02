#!/usr/bin/env python3
N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = []
for i in range(N + 1):
  d = [None] * (S + 1)
  dp.append(d)

dp[0][0] = True

for i in range(N):
  a = A[i]
  for j in range(S + 1):
    if j < a:
      dp[i + 1][j] = dp[i][j]
    else:
      dp[i + 1][j] = dp[i][j] or dp[i][j - a]

if dp[N][S]:
  print('Yes')
else:
  print('No')