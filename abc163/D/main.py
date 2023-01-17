#!/usr/bin/env python3.8
import itertools

mod = 10 **9 + 7
N,K=map(int, input().split())

A = list(range(N + 1))
B = [0] + list(itertools.accumulate(A))
A.reverse()
C = [0] + list(itertools.accumulate(A))
# C.reverse()
A.reverse()

tot = 0
for i in range(K, N + 2):
  l = B[i]
  r = C[i]
  tot += (r - l + 1) % mod
print(tot % mod)