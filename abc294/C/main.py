#!/usr/bin/env python3.8
from bisect import bisect_left


N,M=map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A + B
C.sort()

ps = []
for a in A:
  ps.append(bisect_left(C, a) + 1)
print(*ps)
ps = []
for b in B:
  ps.append(bisect_left(C, b) + 1)
print(*ps)
