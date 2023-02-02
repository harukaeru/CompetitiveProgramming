#!/usr/bin/env python3.8
S = input()
T = input()

dp = []
for i in range(1 + len(S)):
  d = [0] * (1 + len(T))
  dp.append(d)

for i in range(1 + len(S)):
  dp[i][0] = i
for i in range(1 + len(T)):
  dp[0][i] = i

for i in range(1, len(S) + 1):
  for j in range(1, len(T) + 1):
    cost = 0 if S[i - 1] == T[j - 1] else 1
    dp[i][j] = min(
      dp[i][j - 1] + 1,
      dp[i - 1][j] + 1,
      dp[i - 1][j - 1] + cost
    )

print(dp[len(S)][len(T)])