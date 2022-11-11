#!/usr/bin/env python3.8
N = int(input())
K = int(input())

min_d = 999999999999
for i in range(2 ** N):
  d = 1
  p = i
  pp = []
  for j in range(N):
    pp.append(p & (1 << j))
    if (p & (1 << j)) != 0:
      d *= 2
    else:
      d += K
  min_d = min(min_d, d)
print(min_d)