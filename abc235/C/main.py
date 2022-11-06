#!/usr/bin/env python3.8
from collections import defaultdict
N, Q = map(int, input().split())
A = list(map(int, input().split()))

counter = defaultdict(int)
qs = {}
for i in range(N):
  a = A[i]
  counter[a] += 1
  qs[(a, counter[a])] = i

for i in range(Q):
  x, k = map(int, input().split())
  if qs.get((x, k)) is not None:
    print(qs.get((x, k)) + 1)
  else:
    print(-1)
