#!/usr/bin/env python3.8
from collections import Counter
N = int(input())
A = list(map(int, input().split()))

counter = Counter()
for a in A:
  counter[a] += 1

for k, v in counter.items():
  if v == 3:
    print(k)
    exit()