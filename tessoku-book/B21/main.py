#!/usr/bin/env python3.8
N = int(input())
S = input()

dp = []
for i in range(N):
  d = [0] * N
  dp.append(d)

for i in range(N):
  dp[i][i] = 1

  for i in range(N - 1):
    if S[i] == S[i + 1]:
      dp[i][i + 1] = 2
    else:
      dp[i][i + 1] = 1

for le in range(2, N + 1):
  for l in range(N - le):
    r = l + le

    if S[l] == S[r]:
      dp[l][r] = max(dp[l][r - 1], dp[l+1][r], dp[l+1][r-1] + 2)
    else:
      dp[l][r] = max(dp[l][r - 1], dp[l+1][r])

# for d in dp:
#   print(d)

print(dp[0][N - 1])