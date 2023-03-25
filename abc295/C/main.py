#!/usr/bin/env python3.8
from collections import Counter


N = int(input())
A = list(map(int, input().split()))

counter = Counter(A)

cnt = 0
for v in counter.values():
  cnt += v // 2
print(cnt)