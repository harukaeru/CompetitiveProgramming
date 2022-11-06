#!/usr/bin/env python3.8
H, W = map(int, input().split())
HW = []
for i in range(H):
  HW.append(input())

l = []
for j in range(W):
  cnt = 0
  for i in range(H):
    if HW[i][j] == '#':
      cnt += 1
  l.append(cnt)
  

print(*l)