#!/usr/bin/env python3
import math
N = int(input())

cnt = 0
for c in range(1, N):
  ab = N - c
  s = math.sqrt(ab)
  for a in range(1, int(s) + 1):
    if ab % a == 0:
      cnt += 2

  if s == int(s):
    cnt -= 1

print(cnt)