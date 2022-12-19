#!/usr/bin/env python3.8
import math


N = int(input())

cache = {}
accums = [0, 21, 20, 18, 15, 11, 6]
def evaluate(K):
  if K == 1:
    return 7 / 2
  if cache.get(K):
    return cache[K]

  good_e = evaluate(K - 1)
  idx = math.ceil(good_e)
  big_e = accums[idx]
  cnt = (6 - idx + 1)
  small_e = good_e * (6 - cnt)
  cache[K] = (big_e + small_e) /6
  return cache[K]


print(evaluate(N))