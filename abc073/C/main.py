#!/usr/bin/env python3
N = int(input())
A = set()
for i in range(N):
  k = int(input())
  if k in A:
    A.remove(k)
  else:
    A.add(k)

print(len(A))