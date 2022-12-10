#!/usr/bin/env python3.8
from collections import deque
import heapq


N, M, K = map(int, input().split())
A = list(map(int, input().split()))
A = [(a, i) for i, a in enumerate(A)]

B = deque(A[:N -M +2])
print('B', B)
sb = list(sorted(B))
ok = set(sb[:K])
ng = set(sb[K+1:])

s = 0
for b in ok:
  s += b[0]
print(s)

for i in range(1, N - M + 1):
  print('i', i)
  print(ok)
  print(ng)
