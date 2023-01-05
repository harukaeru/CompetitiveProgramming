#!/usr/bin/env python3.8
import itertools

MOD = 998244353
N,M,K = map(int, input().split())

dp = []
for i in range(N + 1):
  if i == 1:
    d = [1] * M
  else:
    d = [0] * M
  dp.append(d)

for i in range(1, N):
  accum = [0] * (M + 2)
  for j in range(M):
    a = j + 1
    v = dp[i][j] % MOD
    accum[0] += v
    accum[M + 1] -= v
    if K != 0:
      accum[max(a - K + 1, 0)] -= v
      accum[min(a + K, M + 1)] += v
  # print('accum', accum)
  dp[i + 1] = list(itertools.accumulate(accum))[1:M + 1]

# for d in dp:
#   print(d)
print(sum(dp[N]) % MOD)