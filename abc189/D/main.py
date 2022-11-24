#!/usr/bin/env python3.8
N = int(input())
S = []
for i in range(N):
  S.append(input())

dp = []
for i in range(N + 1):
  dp.append([0, 0])
# False, True
dp[0] = [1, 1]

for i in range(1, N + 1):
  for x, d in enumerate(dp[i - 1]):
    if S[i - 1] == 'AND':
      dp[i][x and True] += dp[i - 1][x]
      dp[i][x and False] += dp[i - 1][x]
    else:
      dp[i][x or True] += dp[i - 1][x]
      dp[i][x or False] += dp[i - 1][x]

# for d in dp:
#   print(d)
print(dp[N][True])