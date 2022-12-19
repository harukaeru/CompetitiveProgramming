#!/usr/bin/env python3.8
N = int(input())

cache = {}
def evaluate(K):
  if K == 1:
    return 7 / 2
  if cache.get(K):
    return cache[K]

  prev = evaluate(K - 1)

  e = 0
  for i in range(1, 7):
    e += max(i, prev)
  e /= 6
  cache[K] = e
  return cache[K]


print(evaluate(N))