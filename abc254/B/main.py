#!/usr/bin/env python3
N = int(input())

data_0 = [1]
data_1 = [1, 1]
data_2 = [1, 2, 1]

dp = [1]
for i in range(N):
  print(' '.join(map(str, dp)))
  n = [0] + dp + [0]
  dp = []
  for j in range(len(n) - 1):
    dp.append(n[j] + n[j + 1])