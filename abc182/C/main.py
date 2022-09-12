#!/usr/bin/env python3
from itertools import combinations

N = input()
N = list(N)

min_ok = 99999
for i in range(len(N)):
  ch = len(N) - i
  comb = combinations(N, ch)
  for l in comb:
    s = ''.join(l)
    if int(s) % 3 == 0:
      min_ok = min(min_ok, i)

if min_ok == 99999:
  print(-1)
else:
  print(min_ok)
