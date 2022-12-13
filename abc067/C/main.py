#!/usr/bin/env python3.8
import itertools


N = int(input())
A = list(map(int, input().split()))

tot = sum(A)
B = [0] + list(itertools.accumulate(A))
# print(B)
mi = 1e19
for i in range(1, N):
  x = B[i]
  y = tot - x
  mi = min(mi, abs(x - y))
print(mi)