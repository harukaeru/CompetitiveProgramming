#!/usr/bin/env python3.8
N = int(input())
S = []
for i in range(N):
  s = int(input())
  S.append(s)

dp = []
for i in range(1 + N):
  d = [None] * 10001
  dp.append(d)

dp[0][0] = 1

for i in range(1, N + 1):
  for j, v in enumerate(dp[i - 1]):
    if v:
      dp[i][j + S[i - 1]] = v
      dp[i][j] = v

anses = [0]
for i, v in enumerate(dp[N]):
  if v and (i % 10 != 0):
    anses.append(i)
print(max(anses))