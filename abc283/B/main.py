#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
  q, *x = list(map(int, input().split()))
  if q == 1:
    k, x = x
    k -= 1
    A[k] = x
  else:
    k = x[0]
    k -= 1
    print(A[k])