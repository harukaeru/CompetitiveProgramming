#!/usr/bin/env python3
N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in range(Q):
  pawn = A[L[i] - 1]
  if pawn == N:
    continue
  try:
    A.index(pawn + 1)
    continue
  except:
    A[L[i] - 1] = pawn + 1

print(' '.join(map(str, A)))