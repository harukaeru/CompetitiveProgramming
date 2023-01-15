#!/usr/bin/env python3.8
from itertools import accumulate


N = int(input())
A = list(map(int, input().split()))

L = [0] + list(accumulate(A, lambda a, b: max(a, b)))

A.reverse()
R = [0] + list(accumulate(A, lambda a, b: max(a, b)))
R.reverse()

D = int(input())
for i in range(D):
  l,r = map(int, input().split())
  ml = L[l - 1]
  mr = R[r]
  print(max(ml, mr))