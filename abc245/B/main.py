#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

A = set(A)
for i in range(N + 1):
  if i not in A:
    break
print(i)
