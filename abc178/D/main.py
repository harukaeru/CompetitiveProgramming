#!/usr/bin/env python3.8
import sys
sys.setrecursionlimit(300000)

MOD = 10 ** 9 + 7
cache = {}
def f(x):
  if x <= 2:
    return 0

  if x <= 5:
    return 1
  
  if cache.get(x):
    return cache[x]

  cache[x] = (f(x - 1) + f(x - 3)) % MOD
  return cache[x]

S = int(input())
print(f(S) % MOD)