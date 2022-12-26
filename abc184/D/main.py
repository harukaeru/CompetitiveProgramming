#!/usr/bin/env pypy3
A, B, C = map(int, input().split())


cache = {}
def f(x, y, z):
  if x == 100 or y == 100 or z == 100:
    return 0

  if cache.get((x, y, z)):
    return cache[(x, y, z)]

  s = x + y + z
  cache[(x, y, z)] = (
    x / s * (f(x + 1, y, z) + 1)
    + y / s * (f(x, y + 1, z) + 1)
    + z / s * (f(x, y, z + 1) + 1)
  )
  return cache[(x, y, z)]

print(f(A, B, C))