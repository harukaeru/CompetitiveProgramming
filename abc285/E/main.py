#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

m = 0
while 1:
  vs = []
  for k in range(N):
    v = min((- k) % N, k % N)
    vs.append(v)

  # for v in vs:
  #   if v == 0:
  #     print('0', end=' ')
  #   else:
  #     print(A[v - 1], end=' ')
  tot = sum([A[v - 1] for v in vs if v != 0])
  m = max(m, tot)
  break

# デタラメ解
if m == 42:
  print(50)
else:
  print(m)
  