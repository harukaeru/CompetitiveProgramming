#!/usr/bin/env python3
from collections import defaultdict
N = int(input())
A = []
for i in range(N):
  x, y = map(int, input().split())
  A.append((x, y))

S = input()

L = defaultdict(list)
R = defaultdict(list)
ys = set()
for i in range(N):
  x, y = A[i]
  ys.add(y)
  if S[i] == 'L':
    L[y].append(x)
  else:
    R[y].append(x)

for y in ys:
  if len(L[y]) == 0 or len(R[y]) == 0:
    continue
  if min(R[y]) <= max(L[y]):
    print('Yes')
    exit()

print('No')
