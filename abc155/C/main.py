#!/usr/bin/env python3
from collections import Counter
N = int(input())
S = [input() for i in range(N)]

counter = Counter(S)

m = max(counter.values())
for k in sorted(counter.keys()):
  if counter[k] == m:
    print(k)