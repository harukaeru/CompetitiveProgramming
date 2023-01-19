#!/usr/bin/env python3.8
from itertools import accumulate

mod = 998244353

N,K=map(int, input().split())
ranges = []
for i in range(K):
  l,r = map(int, input().split())
  ranges.append((l,r))

dp = [0] * (1 + N)
dp[1] = 1
cums = [0] * (1 + N)
cums[1] = 1

for i in range(2, 1 + N):
  for k in range(K):
    l, r = ranges[k]
    r += 1
    if i - l >= 1:
      dp[i] += cums[i - l]
    if i - r >= 1:
      dp[i] -= cums[i - r]
  dp[i] %= mod
  cums[i] = dp[i] + cums[i - 1]

print(dp[N])