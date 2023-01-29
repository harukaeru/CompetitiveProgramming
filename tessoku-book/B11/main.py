#!/usr/bin/env python3.8
from bisect import bisect_left


N = int(input())
A = list(map(int, input().split()))

B = list(sorted(A))

Q = int(input())
for i in range(Q):
  x = int(input())
  l = -1
  r = N
  while r - l > 1:
    mid = (r + l) // 2
    if B[mid] < x:
      l = mid
    else:
      r = mid
      
  print(r)