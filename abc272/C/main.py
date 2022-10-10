#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))

A.sort()

E = []
O = []

for a in A:
  if a % 2 == 0:
    E.append(a)
  else:
    O.append(a)

m = -1
if len(E) >= 2:
  m = max(m, E[-2] + E[-1])
if len(O) >= 2:
  m = max(m, O[-2] + O[-1])
print(m)