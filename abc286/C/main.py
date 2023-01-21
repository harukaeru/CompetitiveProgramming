#!/usr/bin/env python3.8
from collections import deque


N,A,B=map(int, input().split())
S = input()

T = S * 2

l = N//2
even = N % 2 == 0

m = 1e18
for i in range(N):
  left = T[i:i+l]
  if even:
    right = T[i+l:i+2 * l]
  else:
    right = T[i+l + 1:1+i+2 * l]

  cnt = 0
  for j in range(l):
    cnt += left[j] != right[l - 1 - j]
  res = A * i + cnt * B
  m = min(m, res)
  
  # print(left, right, res)
  # print('----')
print(m)