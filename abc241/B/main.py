#!/usr/bin/env python3.8
from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

repo = Counter(A)

for b in B:
  if repo[b] > 0:
    repo[b] -= 1
  else:
    print('No')
    exit()
print('Yes')