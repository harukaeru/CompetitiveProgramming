#!/usr/bin/env python3.8
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

S = set(A)
M = max(A)

cnt = 0
bucket = defaultdict(int)
for a in A:
  for b in range(a, M + 1, a):
    if b in S:
      bucket[b] += 1

print(len([v for v in bucket.values() if v == 1]))