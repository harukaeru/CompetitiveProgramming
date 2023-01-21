#!/usr/bin/env python3.8
N,P,Q,R,S = map(int, input().split())
A = list(map(int, input().split()))

for j in range(0, (Q - P) + 1):
  A[P - 1 + j], A[R - 1 + j] = A[R - 1 + j], A[P - 1 + j]

print(*A)