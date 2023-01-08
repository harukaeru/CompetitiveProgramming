#!/usr/bin/env pypy3

from math import sqrt

def factorization(x):
  m = int(x ** (1/3)) + 1
  
  for i in range(2, m):
    if x % i == 0:
      x //= i
      if x % i == 0:
        return [i, x//i]
      else:
        return [int(sqrt(x)), i]

T = int(input())
for i in range(T):
  N = int(input())

  x = factorization(N)
  print(*x)