#!/usr/bin/env python3.8
N,S=map(int, input().split())
A = list(map(int, input().split()))

dp = []
for i in range(N + 1):
  d = [False] * (1 + S)
  dp.append(d)

dp[0][0] = True

for i in range(1, N + 1):
  a = A[i - 1]
  for j in range(0, S + 1):
    dp[i][j] = dp[i][j] or dp[i - 1][j]
    if j + a <= S:
      dp[i][j + a] = dp[i][j + a] or dp[i - 1][j]

if dp[N][S]:
  print('Yes')
else:
  print('No')