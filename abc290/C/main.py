#!/usr/bin/env python3.8
from collections import Counter
import heapq


N,K=map(int, input().split())
A = list(map(int, input().split()))

C = set(A)
c = -1
for i in range(K):
  if i in C:
    c = i
  else:
    break
print(c + 1)