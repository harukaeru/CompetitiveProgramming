#!/usr/bin/env pypy3
N,X = map(int, input().split())
P = []
for i in range(N):
  a,b=map(int, input().split())
  P.append((a,b))

dp = []
for i in range(N + 1):
  dp.append([0] * (X + 1))

dp[0][0] = 1

for i in range(1, N + 1):
  p = P[i - 1]
  a, b = p
  for j in range(X + 1):
    if dp[i - 1][j] == 0:
      continue
    for c in range(0, a * b + 1, a):
      if j + c < X + 1 and dp[i - 1][j]:
        dp[i][j + c] = 1

  # print(dp)

if dp[N][X]:
  print('Yes')
else:
  print('No')