#!/usr/bin/env python3.8
from collections import Counter
X = list(map(int, input().split()))
counter = Counter(X)

for k, v in counter.items():
  if v % 2 == 1:
    print(k)