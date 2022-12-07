#!/usr/bin/env python3.8
from itertools import permutations


N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
# print('A', A)
B = [str(a) for a in A[:3]]
mp = ''
for p in permutations(B):
  pp = ''.join(p)
  mp = max(mp, pp)
# print(B)
# print(''.join(B))
print(mp)