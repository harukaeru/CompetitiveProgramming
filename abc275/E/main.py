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

# print('N', N)
anses = []
for i in range(1, K + 1):
  for p in range(N + 1):
    for j in range(1, M + 1):
      # import sys; sys.stdin = open("/dev/tty"); breakpoint()

      if j + p <= N:
        dp[i][j + p] += dp[i - 1][p]
      else:
        dp[i][2 * N - (j + p)] += dp[i - 1][p]
  x = sum(dp[i])
  ok = dp[i][N]
  dp[i][N] = 0
  anses.append((ok, M ** i))

s = 0
for ans in anses:
  m = modinv(ans[1])
  s += m * ans[0]
  s %= MOD
print(s)