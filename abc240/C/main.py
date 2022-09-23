#!/usr/bin/env python3
N, X = map(int, input().split())
P = []
for i in range(N):
  a, b = map(int, input().split())
  P.append((a, b))

dp = [0] * 10001
dp[0] = 1

for i in range(N):
  ndp = [0] * 10001
  a, b = P[i]
  for pos, cnt in enumerate(dp):
    if pos + a <= X:
      ndp[pos + a] += dp[pos]
    if pos + b <= X:
      ndp[pos + b] += dp[pos]
  dp = ndp

if dp[X]:
  print('Yes')
else:
  print('No')
