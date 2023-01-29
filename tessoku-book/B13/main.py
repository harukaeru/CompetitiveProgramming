#!/usr/bin/env python3.8
import itertools


N,K=map(int, input().split())
A = list(map(int, input().split()))

B = [0] + list(itertools.accumulate(A))

l = 0
r = 0
tot = 0
while l < N:
  while r + 1 <= N and B[r + 1] - B[l] <= K:
    r += 1
  tot += r - l

  if l == r:
    r += 1
  l += 1

print(tot)