#!/usr/bin/env python3.8
N,Q=map(int, input().split())
d = [0] * N
for i in range(Q):
  q, x = map(int, input().split())
  if q == 1:
    d[x - 1] += 1
  elif q == 2:
    d[x - 1] += 2
  elif q == 3:
    if d[x - 1] >= 2:
      print('Yes')
    else:
      print('No')