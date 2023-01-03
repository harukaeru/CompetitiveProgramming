#!/usr/bin/env python3.8
MOD = 10 ** 9 + 7
cache = {}
def f(x):
  if x <= 2:
    return 0

  if x <= 5:
    return 1
  
  if cache.get(x):
    return cache[x]

  s = 1
  for i in range(3, x - 3 + 1):
    s += f(i) % MOD
  cache[x] = s
  return s

S = int(input())
print(f(S) % MOD)