#!/usr/bin/env python3.8
N = int(input())
S = []
for i in range(N):
  S.append(input())

for j in range(N):
  s = ''
  for i in range(N - 1, -1, -1):
    s += S[i][j]
  print(s)
