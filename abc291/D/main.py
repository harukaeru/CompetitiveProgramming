#!/usr/bin/env python3.8
N = int(input())
mod = 998244353

A = []
B = []
for i in range(N):
  a,b = map(int, input().split())
  A.append(a)
  B.append(b)

dp = []
for i in range(N):
  d = [0, 0]
  dp.append(d)

dp[0] = [1, 1]

for i in range(1, N):
  if A[i] != A[i - 1]:
    dp[i][0] += dp[i - 1][0]
  if A[i] != B[i - 1]:
    dp[i][0] += dp[i - 1][1]

  if B[i] != A[i - 1]:
    dp[i][1] += dp[i - 1][0]
  if B[i] != B[i - 1]:
    dp[i][1] += dp[i - 1][1]

  dp[i][0] %= mod
  dp[i][1] %= mod

# for d in dp:
#   print(d)
print(sum(dp[N - 1]) % mod)