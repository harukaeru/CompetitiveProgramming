#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

def color(v):
  if v <= 399:
    return 1
  if v <= 799:
    return 2
  if v <= 1199:
    return 3
  if v <= 1599:
    return 4
  if v <= 1999:
    return 5
  if v <= 2399:
    return 6
  if v <= 2799:
    return 7
  if v <= 3199:
    return 8
  return None


free_count = 0
orig = set()
for i in range(N):
  a = A[i]
  col = color(a)
  if col is None:
    free_count += 1
  else:
    orig.add(col)

mi = max(len(orig), 1)
ma = len(orig) + free_count
print(mi, ma)