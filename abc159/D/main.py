#!/usr/bin/env python3.8
from collections import Counter
from math import comb

N = int(input())
A = list(map(int, input().split()))

counter = Counter(A)
tot = sum(comb(v, 2) for v in counter.values())

for a in A:
  k = counter[a]
  print(tot - comb(k, 2) + comb(k - 1, 2))