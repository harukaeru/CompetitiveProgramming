#!/usr/bin/env pypy3
N, M = map(int, input().split())
A = list(map(int, input().split()))

minf = -999999999999

dp = []
for d in range(N + 1):
  d = [0]
  for m in range(M):
    d.append(minf)
  dp.append(d)
dp[0][0] = 0

for i in range(1, N + 1):
  a = A[i - 1]
  for j in range(1, M + 1):
    addition = j * a
    dp[i][j] = max(dp[i - 1][j - 1] + addition, dp[i - 1][j])

# for d in dp:
#   print(d)
print(dp[N][M])