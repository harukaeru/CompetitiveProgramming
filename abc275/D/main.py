#!/usr/bin/env python3.8
N = int(input())

cache = {}
def f(k):
  if k == 0:
    return 1
  if cache.get(k):
    return cache[k]
  
  ret = f(k // 2) + f(k // 3)
  cache[k] = ret
  return ret

print(f(N))