#!/usr/bin/env python3
N, K = map(int, input().split())
A = list(map(int, input().split()))

count = sum(A)
if K < count:
  print('No')
  exit()

if (K - count) % 2 == 0:
  print('Yes')
else:
  print('No')