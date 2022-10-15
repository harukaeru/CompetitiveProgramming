#!/usr/bin/env python3
N = int(input())

def f(k):
  if k == 0:
    return 1
  return k * f(k - 1)

print(f(N))