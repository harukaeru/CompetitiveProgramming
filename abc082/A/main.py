#!/usr/bin/env python3.8
from collections import Counter
N = int(input())
a = list(map(int, input().split()))

counter = Counter(a)

r = 0
for c in counter.keys():
  r += counter[c] - c

print(r)
