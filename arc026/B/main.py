#!/usr/bin/env python3.8
import math
N = int(input())

if N == 1:
  print('Deficient')
  exit()

m = int(math.sqrt(N)) + 1
k = set([1])
for a in range(2, m):
  if N % a == 0:
    b = N // a
    k.add(a)
    k.add(b)

# print('k', k)
k = sum(k)
if k == N:
  print('Perfect')
elif k > N:
  print('Abundant')
else:
  print('Deficient')