#!/usr/bin/env python3.8
N = int(input())

A = []
for i in range(N):
  A.append(int(input()))

l = list(set(A))
l.sort()

print(l[-2])