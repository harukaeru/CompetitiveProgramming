#!/usr/bin/env python3.8
N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

B = set(A)

for i in range(N):
  if A[i] + X in B:
    print('Yes')
    exit()
print('No')