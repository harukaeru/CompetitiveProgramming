#!/usr/bin/env pypy3
mod = 998244353
N,M=map(int, input().split())

x = list(range(1, M + 1))

dp = []
for i in range(N + 1):
  aa = []
  for a in range(M  + 2):
    bb = []
    for b in range(M  + 2):
      c = [0] * (M + 2)
      bb.append(c)
    aa.append(bb)
  dp.append(aa)

dp[0][M + 1][M + 1][M + 1] = 1

for i in range(N):
  for a in range(1, M + 2):
    for b in range(1, M + 2):
      for c in range(1, M + 2):
        for x in range(1, M + 1):
          if x <= a:
            dp[i + 1][x][b][c] += dp[i][a][b][c]
            dp[i + 1][x][b][c] %= mod
          elif x <= b:
            dp[i + 1][a][x][c] += dp[i][a][b][c]
            dp[i + 1][a][x][c] %= mod
          elif x <= c:
            dp[i + 1][a][b][x] += dp[i][a][b][c]
            dp[i + 1][a][b][x] %= mod

ans = 0
for a in range(1, M + 1):
  for b in range(1, M + 1):
    for c in range(1, M + 1):
      ans += dp[N][a][b][c]

ans %= mod
print(ans)