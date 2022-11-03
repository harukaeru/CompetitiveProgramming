#!/usr/bin/env python3
from collections import Counter
X = map(int, input().split())

c = Counter(X)
for k, v in c.items():
  if v == 1:
    print(k)

