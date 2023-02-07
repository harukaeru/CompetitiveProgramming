#!/usr/bin/env python3.8
N,M=map(int, input().split())
A = []
for i in range(M):
  X = list(map(int, input().split()))
  A.append(X)

dp = []
for i in range(M + 1):
  d = [1e18] * (2 ** N)
  dp.append(d)

dp[0][0] = 0

for i in range(1, M + 1):
  X = A[i - 1]
  v = int(''.join(map(str, X)), 2)

  for j in range(2 ** N):
    dp[i][j] = min(dp[i][j], dp[i - 1][j])
    dp[i][v | j] = min(dp[i][v | j], dp[i - 1][j] + 1)

ans = dp[M][2**N - 1]
if ans == 1e18:
  print(-1)
else:
  print(ans)