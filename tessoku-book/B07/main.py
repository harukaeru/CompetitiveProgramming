#!/usr/bin/env python3.8
import itertools


T = int(input())
N = int(input())

times = [0] * (2 + T)
for i in range(N):
  l, r = map(int, input().split())
  times[l] += 1
  times[r] -= 1

# print(times)
times = list(itertools.accumulate(times))
for i in range(0, T):
  print(times[i])