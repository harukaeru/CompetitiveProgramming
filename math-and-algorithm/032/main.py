#!/usr/bin/env python3
N, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

l = 0
r = N

while r - l > 1:
  mid = (r + l) // 2
  if A[mid] == X:
    print('Yes')
    exit()
  if A[mid] < X:
    l = mid
  else:
    r = mid

print('No')