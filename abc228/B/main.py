#!/usr/bin/env python3.8
N, X = map(int, input().split())
A = list(map(int, input().split()))

known = set()

while X not in known:
  known.add(X)
  X = A[X - 1]

print(len(known))