#!/usr/bin/env python3
import math
from collections import Counter
N = int(input())

S = []
for i in range(N):
  s = list(input())
  s.sort()
  s = ''.join(s)
  S.append(s)

counter = Counter(S)
# print(counter)

total = 0
for value in counter.values():
  if value == 1:
    continue

  total += math.comb(value, 2)

print(total)