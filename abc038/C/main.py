#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

l,r = 0, 0
cur = None

tot = N
while l < N:
  k = r
  while r < N:
    if cur is None:
      cur = A[r]
    else:
      if cur < A[r]:
        cur = A[r]
        k = r
      else:
        break
    r += 1
  
  if k >= l:
    tot += (k - l)
    l += 1
    r = k
  else:
    r += 1
    cur = None

print(tot)