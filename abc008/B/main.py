#!/usr/bin/env python3.8
from collections import Counter


N = int(input())
counter = Counter()
for i in range(N):
  counter[input()]+= 1

max_v = -1
m = None
for k, v in counter.items():
  if v > max_v:
    max_v = v
    m = k

print(m)
