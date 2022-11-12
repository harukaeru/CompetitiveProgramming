#!/usr/bin/env python3.8
N, Q = map(int, input().split())
A = [0] * N
for i in range(Q):
  l, r, t = map(int, input().split())
  for j in range(l - 1, r):
    A[j] = t

for a in A:
  print(a)