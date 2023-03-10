#!/usr/bin/env python3.8
from collections import Counter


N,M=map(int, input().split())
A = list(map(int, input().split()))
counter = Counter(A)
for i in range(M):
  b,c=map(int, input().split())
  counter[c] += b
# print(counter)
keys = list(counter.keys())
keys.sort(reverse=True)

tot = 0
for k in keys:
  cnt = counter[k]
  if N >= cnt:
    N -= cnt
    tot += k * cnt
  else:
    tot += k * N
    break
print(tot)