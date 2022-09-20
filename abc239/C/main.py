#!/usr/bin/env python3
x1, y1, x2, y2 = map(int, input().split())

ds = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

for d1 in ds:
  for d2 in ds:
    if x2 + d2[0] == x1 + d1[0] and y2 + d2[1] == y1 + d1[1]:
      print('Yes')
      exit()
print('No')