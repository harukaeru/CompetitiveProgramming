#!/usr/bin/env python3.8
H,W=map(int, input().split())
A = []
for i in range(H):
  a = list(map(int, input().split()))
  A.append(a)

for i in range(H):
  s = ''
  for j in range(W):
    if A[i][j] == 0:
      s += '.'
    else:
      s += chr(ord('A') + A[i][j] - 1)
  print(s)
  