#!/usr/bin/env python3.8
N = int(input())

def f(x):
  return x ** 3 + x

l = -N - 1
r = N + 1

while r - l > 0.000001:
  mid = (r + l) / 2
  a = f(mid)
  if a >= N:
    r = mid
  else:
    l = mid

print(r)