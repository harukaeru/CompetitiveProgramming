#!/usr/bin/env python3
from itertools import permutations
X = int(input())

a = []
while X > 0:
  a.append(X % 2)
  X //= 2

b = []
for i, v in enumerate(a):
  if v == 1:
    b.append(i)

b = [2 ** i for i in b]
l = []
for k in range(2 ** len(b)):
  q = k
  d = 0
  for i in range(len(b)):
    if q % 2:
      d += b[i]
    q //= 2
  l.append(d)

l.sort()
for ll in l:
  print(ll)