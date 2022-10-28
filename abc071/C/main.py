#!/usr/bin/env python3
from collections import Counter
N = int(input())
A = list(map(int, input().split()))

counter = Counter(A)

area = 0
for k in reversed(sorted(counter.keys())):
  if counter[k] >= 4:
    area = max(area, k * k)

A = [k for k, v in counter.items() if v >= 2]
A.sort()

if len(A) >= 2:
  area = max(area, A[-1] * A[-2])
  print(area)
else:
  print(0)