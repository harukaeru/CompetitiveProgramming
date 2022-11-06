#!/usr/bin/env python3.8
from collections import Counter
N = int(input())
a = list(map(int, input().split()))

counter = Counter(a)

r = 0
for c in counter.keys():
  # 全部取り除く
  if c > counter[c]:
    r += counter[c]
  else:
    r += counter[c] - c

print(r)

