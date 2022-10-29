#!/usr/bin/env python3
N, M, K = map(int, input().split())
MOD = 998244353

def modinv(x):
  p = MOD - 2
  y = x
  ans = 1
  for i in range(60):
    if (p & (1 << i)) != 0:
      ans *= y
      ans %= MOD
    y *= y
    y %= MOD
  return ans

anses = []
dp = []
for i in range(K + 1):
  d = [0] * (N + 1)
  dp.append(d)
dp[0][0] = 1

x = 0
ok = 0
print('N', N)
for i in range(1, K + 1):
  print(i, '-----------------')
  print('b', dp[i])
  for p in range(N + 1):
    for j in range(1, M + 1):
      if j + p <= N:
        dp[i][j + p] += dp[i - 1][p]
      else:
        if (j + p) // N % 2 == 0:
          dp[i][(j + p + N) % (N + 1)] += dp[i - 1][p]
        else:
          dp[i][(j + p) % (N + 1)] += dp[i - 1][p]
  if dp[i][N]:
    ok += dp[i][N]
    print('ok->', dp[i][N])
    dp[i][N] = 0
  print('a', dp[i])
  print('ok', ok)
  x += sum(dp[i])
  print('sum', sum(dp[i]))
  print('x', x)

ans = ok, (ok + x)
m = modinv(ans[1])
print(m * ans[0] % MOD)