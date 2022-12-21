#!/usr/bin/env python3.8
from collections import Counter

N = int(input())
A = list(map(int, input().split()))

counter = Counter(A)
S = set(A)
A.sort()
M = max(A)
# print(A)

cnt = 0
ng = set()
for i in range(N):
  a = A[i]
  if counter[a] >= 2:
    ng.add(a)
  for b in range(2 * a, M + 1, a):
    if b in S:
      ng.add(b)

print(len(S) - len(ng))