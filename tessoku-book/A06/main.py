#!/usr/bin/env python3.8
import itertools


N,Q = map(int, input().split())
A = list(map(int, input().split()))
B = [0] + list(itertools.accumulate(A))

for i in range(Q):
  l,r = map(int, input().split())
  print(B[r]-B[l-1])