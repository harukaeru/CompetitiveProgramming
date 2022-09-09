#!/usr/bin/env python3
import math
N = int(input())
xy = []
for i in range(N):
  x, y = map(int, input().split())
  xy.append((x, y))

for i in range(N - 2):
  for j in range(i + 1, N - 1):
    for k in range(j + 1, N):
      x1, y1 = xy[i]
      x2, y2 = xy[j]
      x3, y3 = xy[k]
      x1 -= x3
      x2 -= x3
      y1 -= y3
      y2 -= y3

      if x1 * y2 == x2 * y1:
        print('Yes')
        exit()

print('No')