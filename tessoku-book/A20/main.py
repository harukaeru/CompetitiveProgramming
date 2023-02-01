#!/usr/bin/env python3.8
S = input()
T = input()

if len(T) > len(S):
  S,T=T,S

dp = []
for i in range(len(S) + 1):
  dp.append([0] * (len(T) + 1))
    
for i in range(1, len(S) + 1):
  s = S[i - 1]
  for j in range(1, len(T) + 1):
    t = T[j - 1]
    if s != t:
      dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])
    else:
      dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)

print(dp[len(S)][len(T)])