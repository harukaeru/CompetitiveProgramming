#!/usr/bin/env python3.8
import itertools


N, W = map(int, input().split())
M = 2 * (10 ** 5) + 1
times = [0] * (M)

for i in range(N):
  s,t,p = map(int, input().split())
  times[s] += p
  times[t] -= p

A = itertools.accumulate(times)
if max(A) > W:
  print('No')
else:
  print('Yes')