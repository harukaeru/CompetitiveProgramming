#!/usr/bin/env python3.8
from collections import defaultdict
N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
# print(A)

groups = defaultdict(int)
i = 0
while i < N:
  # print('i', i)
  a = A[i]
  groups[a] += a
  while i + 1 < N and (A[i] == A[i + 1] or ((A[i] + 1) % M) == A[i + 1]):
    i += 1
    groups[a] += A[i]
  i += 1

# del groups[0]
L = list(sorted(groups.keys()))
if len(L) > 1:
  if (A[N-1] + 1)% M == 0 and A[0] == 0:
    groups[0] += groups[L[-1]]
    del groups[L[-1]]

# print(groups)
# print(sum(A))
# print(list(groups.values()))
# print('group', groups)
print(sum(A) - max(groups.values()))