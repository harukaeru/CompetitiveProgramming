#!/usr/bin/env python3
N = int(input())

cnt = 0
for i in range(1, N + 1):
  # i * j == 平方数となるような最小のjをkとする。kの最大値はi
  k = i
  
  # kを平方数で割りまくり、残ったkに平方数をかけたものが答えになる
  d = 2
  while d * d <= k:
    while k % (d * d) == 0:
      k //= d * d
    d += 1

  d = 1
  while k * d * d <= N:
    cnt += 1
    d += 1

print(cnt)