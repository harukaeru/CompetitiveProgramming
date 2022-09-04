#!/usr/bin/env python3
import math
N = int(input())

min_d = 9999999999999
m = int(math.sqrt(N)) + 1
for i in range(1, m + 1):
  if N % i != 0:
    continue

  j = N // i

  d = abs(i - 1) + abs(j - 1)
  min_d = min(min_d, d)

print(min_d)