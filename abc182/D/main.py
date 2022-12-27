#!/usr/bin/env python3.8
import itertools


N = int(input())
A = list(map(int, input().split()))

B = list(itertools.accumulate(A))
M = [0]
for i in range(N):
  M.append(max(B[i], M[i]))

s = 0
t = 0
for i in range(N):
  m = s + M[i + 1]
  t = max(t, m)
  s += B[i]
print(t)