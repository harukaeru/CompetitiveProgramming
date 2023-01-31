#!/usr/bin/env python3.8
from bisect import bisect_left


N = int(input())
A = list(map(int, input().split()))

C = list(set(A))
C.sort()

B = []
for a in A:
  idx = bisect_left(C, a)
  B.append(idx + 1)
  
print(*B)