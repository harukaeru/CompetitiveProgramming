#!/usr/bin/env python3.8
from bisect import bisect_left


N,X=map(int, input().split())
A = list(map(int, input().split()))
r = N
l = -1
ans = None
while r - l > 1:
  mid = (r + l) // 2
  if A[mid] == X:
    ans = mid
    break
  elif A[mid] > X:
    r = mid
  else:
    l = mid
print(ans + 1)