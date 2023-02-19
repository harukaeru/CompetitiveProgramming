#!/usr/bin/env python3.8
N,M=map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s = 0
for b in B:
  s += A[b - 1]
print(s)