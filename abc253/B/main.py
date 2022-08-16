#!/usr/bin/env python3
H, W = map(int, input().split())
S = []
for i in range(H):
  S.append(input())

c = []
for i in range(H):
  for j in range(W):
    if S[i][j] == 'o':
      c.append((i, j))

print(abs(c[0][0] - c[1][0]) + abs(c[0][1] - c[1][1]))