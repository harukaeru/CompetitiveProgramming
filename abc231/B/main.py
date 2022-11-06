#!/usr/bin/env python3.8
from collections import Counter
N = int(input())
counter = Counter()
for i in range(N):
  counter[input()] += 1

max_v = -1
candidate = None
for k, v in counter.items():
  if max_v < v:
    max_v = v
    candidate = k

print(candidate)