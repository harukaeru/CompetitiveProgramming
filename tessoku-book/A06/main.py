#!/usr/bin/env python3.8
import itertools


N,Q = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * (1 + N)
for i in range(1, N + 1):
  B[i] = A[i - 1] + B[i - 1]

for i in range(Q):
  l,r = map(int, input().split())
  print(B[r]-B[l-1])