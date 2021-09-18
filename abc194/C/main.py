#!/usr/bin/env python3
from collections import Counter

N = int(input())
*A, = map(int, input().split())


counter = Counter(A)

keys = list(counter.keys())

s = 0
for i in keys:
    for j in keys:
        x = (i - j) * (i - j)
        s += counter[i] * counter[j] * x
print(s // 2)
