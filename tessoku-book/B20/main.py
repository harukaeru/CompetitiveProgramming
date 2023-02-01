#!/usr/bin/env python3.8
S = input()
T = input()

if len(T) > len(S):
  S,T=T,S

dp = []
for i in range(len(S) + 1):
  dp.append([1e18] * (len(T) + 1))

for i in range(len(S) + 1):
  dp[i][0] = i
for i in range(len(T) + 1):
  dp[0][i] = i

for i in range(1, len(S) + 1):
  for j in range(1, len(T) + 1):
    s = S[i - 1]
    t = T[j - 1]
    cost = 0 if s == t else 1
    dp[i][j] = min(
      dp[i - 1][j - 1] + cost,
      dp[i][j - 1] + 1,
      dp[i - 1][j] + 1
    )

print(dp[len(S)][len(T)])  