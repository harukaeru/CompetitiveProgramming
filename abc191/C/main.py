#!/usr/bin/env python3.8
H, W = map(int, input().split())
S = []
for i in range(H):
  S.append(input())

v = 0
for x in range(1, H):
  for y in range(1, W):
    b = int(S[x - 1][y - 1] == '#')
    b += int(S[x - 1][y] == '#')
    b += int(S[x][y - 1] == '#')
    b += int(S[x][y] == '#')
    if b == 1 or b == 3:
      v += 1

print(v)