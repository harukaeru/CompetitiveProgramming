#!/usr/bin/env python3.8
N, S = map(int, input().split())
X = []
for i in range(N):
  a, b = map(int, input().split())
  X.append((a, b))

dp = [None] * (S + 1)
dp[0] = ''

for i in range(N):
  ndp = [None] * (S + 1)
  for j in range(S):
    if dp[j] is not None and j + X[i][0] <= S:
      ndp[j + X[i][0]] = dp[j] + 'H'
    if dp[j] is not None and j + X[i][1] <= S:
      ndp[j + X[i][1]] = dp[j] + 'T'
  dp = ndp
  # print(dp)

if ndp[S]:
  print('Yes')
  print(ndp[S])
else:
  print('No')