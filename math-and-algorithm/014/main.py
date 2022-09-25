#!/usr/bin/env python3
import math
N = int(input())

def calc(n):
  a = 1
  b = n
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      a, b = i, n // i
      break
  if a == 1:
    return [b]
  calced = calc(b)
  return [a, *calced]

print(*calc(N))