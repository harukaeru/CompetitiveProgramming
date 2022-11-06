#!/usr/bin/env python3.8
R, C = map(int, input().split())

d = max(abs(R - 8), abs(C - 8))
if d % 2 == 1:
  print('black')
else:
  print('white')