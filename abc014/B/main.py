#!/usr/bin/env python3.8
n, X = map(int, input().split())
A = list(map(int, input().split()))

tot = 0
for i in range(n):
  if (X & (1 << i)) != 0:
    tot += A[i]

print(tot)