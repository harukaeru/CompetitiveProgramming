#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

P = 0

bases = []
for a in A:
  bases.append(0)
  n_bases = []
  for b in bases:
    n = b + a
    if n >= 4:
      P += 1
    else:
      n_bases.append(n)
  bases = n_bases
  
print(P)
