#!/usr/bin/env python3.8
N, L = map(int, input().split())
A = list(map(int, input().split()))

mi = -1
for i in range(N):
  a = A[i]
  if a == 2:
    mi = max(mi, i)
if mi == -1:
  print('Yes')
  exit()

s = 0
for i in range(mi):
  a = A[i]
  s += a + 1

if L - s >= 2:
  print('Yes')
else:
  print('No')