#!/usr/bin/env pypy3
from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
Q = int(input())

d = None

for i in range(Q):
  q, *p = map(int, input().split())
  if q == 1:
    x = p[0]
    A = defaultdict(int)
    d = x
  if q == 2:
    i, x = p
    if d is None:
      A[i - 1] += x

    else:
      if A.get(i - 1):
        A[i - 1] += x
      else:
        A[i - 1] = d + x
  
  if q == 3:
    i = p[0]
    if d is None:
      print(A[i - 1])
    else:
      print(A.get(i - 1, d))