#!/usr/bin/env python3.8
from collections import Counter
from math import comb


S = input()

A = []
for i in range(1 + len(S)):
  A.append([0] * 10)

for i in range(len(S)):
  for j in range(10):
    A[i + 1][j] = A[i][j]
  v = ord(S[i]) - ord('0')
  A[i + 1][v] += 1
  A[i + 1][v] %= 2

counter = Counter()
for a in A:
  t = tuple(a)
  counter[t] += 1

# print(counter)

tot = 0
for v in counter.values():
  if v >= 2:
    tot += comb(v, 2)
print(tot)