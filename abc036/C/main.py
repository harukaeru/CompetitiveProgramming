#!/usr/bin/env python3.8
N = int(input())
A = []
for i in range(N):
  A.append(int(input()))

B = set(A)
B = sorted(list(B))
conv = dict()
for i, b in enumerate(B):
  conv[b] = i

for i in range(N):
  print(conv[A[i]])