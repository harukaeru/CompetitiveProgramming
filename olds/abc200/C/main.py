#!/usr/bin/env python3
from math import comb
from collections import Counter
N = int(input())
*A, = map(int, input().split())

modded_A = []
for i in range(N):
    a = A[i]
    modded_A.append(a % 200)

# print('m', modded_A)
c = Counter(modded_A)
s = 0
for v in c.values():
    s += comb(v, 2)
print(s)
