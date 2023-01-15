#!/usr/bin/env python3.8
import itertools


H,W,N = map(int, input().split())

snows = []
for i in range(H + 2):
  s = [0] * (W + 2)
  snows.append(s)

for i in range(N):
  a,b,c,d=map(int, input().split())
  snows[a][b] += 1
  snows[c+1][b] -= 1
  snows[a][d + 1] -= 1
  snows[c+1][d + 1] += 1

for i in range(1, H + 2):
  snows[i] = list(itertools.accumulate(snows[i]))

for j in range(1, W + 2):
  accum = [0] * (H + 2)
  for i in range(1, H + 2):
    accum[i] = accum[i - 1] + snows[i][j]
  
  for i, a in enumerate(accum):
    snows[i][j] = a

for i in range(1, H + 1):
  print(*snows[i][1:W+1])