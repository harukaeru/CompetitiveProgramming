#!/usr/bin/env pypy3

MOD = 998244353
N = int(input())
A = list(map(int, input().split()))

def search(n, cnt):
  dp = []
  for i in range(N + 1):
    dd = []
    for j in range(cnt + 1):
      d = [0] * (n)
      dd.append(d)
    dp.append(dd)
  dp[0][0][0] = 1
  # print(dp)

  # i個目で、counter個すでにえらんでいて、j mod nになる
  for i in range(1, N + 1):
    chosen = A[i - 1]
    for counter in range(1, cnt + 1):
      for j in range(n):
        dp[i][counter][(j + chosen) % n] += dp[i - 1][counter - 1][j]
        dp[i][counter - 1][(j + chosen) % n] += dp[i - 1][counter - 1][(j + chosen) % n]
  # for dd in dp:
  #   print('-----')
  #   for d in dd:
  #     print(d)
  return dp

tot = 0
for i in range(1, N + 1):
  tot += search(i, N)[N][i][0] % MOD
print(tot % MOD)