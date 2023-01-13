#!/usr/bin/env python3.8
H,W = map(int, input().split())
HW = []
for i in range(H):
  X = list(map(int, input().split()))
  HW.append(X)

S = []
for i in range(H + 1):
  S.append([0] * (W + 1))

for i in range(1, H + 1):
  for j in range(1, W + 1):
    s = 0
    if i - 1 >= 0:
      s += S[i - 1][j]
    if j - 1 >= 0:
      s += S[i][j - 1]
    if j - 1 >= 0 and j - 1 >= 0:
      s -= S[i - 1][j - 1]
    s += HW[i - 1][j - 1]
    S[i][j] = s

Q = int(input())
for i in range(Q):
  a,b,c,d=map(int, input().split())
  print(S[c][d] - S[a - 1][d] - S[c][b - 1] + S[a - 1][b - 1])