#!/usr/bin/env python3.8
from collections import Counter
S = input()

counter = Counter()
for s in S:
  counter[s] += 1

for k, v in counter.items():
  if v == 1:
    print(k)
    exit()

print(-1)
