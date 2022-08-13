#!/usr/bin/env python3
H, W = map(int, input().split())

A = []
for i in range(H):
  A.append(list(map(int, input().split())))


B = []
for j in range(W):
  w = []
  for i in range(H):
    w.append(A[i][j])
  B.append(w)

for b in B:
  print(' '.join(map(str, b)))
