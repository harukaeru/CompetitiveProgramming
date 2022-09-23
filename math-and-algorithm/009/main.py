#!/usr/bin/env python3
N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * (S + 1)
dp[0] = 1

for i in range(N):
  ndp = [0] * (S + 1)
  a = A[i]
  for j, _ in enumerate(dp):
    if j + a <= S:
      ndp[j + a] += dp[j]
    ndp[j] += dp[j]
  dp = ndp

if dp[S]:
  print('Yes')
else:
  print('No')