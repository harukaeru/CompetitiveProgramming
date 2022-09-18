#!/usr/bin/env python3
from numba import njit
import math
N = int(input())

@njit
def solve():
  cnt = 0
  for i in range(1, int(math.pow(N, 1/3)) + 2):
    p = N // i
    for j in range(i, int(math.sqrt(p)) + 2):
      m = p // j
      if m >= j:
        l = m - j + 1
        cnt += l
        # print('  j', i, j, p // j)
        # print('  l', l)
  print(cnt)

solve()