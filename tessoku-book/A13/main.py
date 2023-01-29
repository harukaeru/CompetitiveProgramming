#!/usr/bin/env python3.8
from math import comb


N,K=map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = 0
tot = 0
while l < N:
  while r + 1 < N and abs(A[l] - A[r + 1]) <= K:
    r += 1
  cnt = r - l
  tot += cnt
  if l == r:
    r += 1
  l += 1
print(tot)