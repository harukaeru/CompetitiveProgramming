#!/usr/bin/env python3.8
import itertools


D = int(input())
N = int(input())

days = [0] * (2 + D)
for i in range(N):
  l,r = map(int, input().split())
  days[l] += 1
  days[r + 1] -= 1

A  =list(itertools.accumulate(days))
for i in range(1, D + 1):
  print(A[i])