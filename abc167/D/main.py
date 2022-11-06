#!/usr/bin/env python3.8
import math
N, K = map(int, input().split())
A = list([a - 1 for a in map(int, input().split())])

nex = 1

d = math.ceil(math.log(K, 2))


dp = []
for i in range(d + 1):
  dd = [-1] * N
  dp.append(dd)

dp[0] = A

for i in range(d):
  for v in range(N):
    dp[i + 1][v] = dp[i][dp[i][v]]

v = 0
for i in range(d + 1):
  if (K & (1 << i)) != 0:
    # print('i', i)
    # print('here', v)
    # print(dp[i])
    v = dp[i][v]

print(v + 1)