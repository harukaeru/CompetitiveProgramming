#!/usr/bin/env python3.8
import math
N, K = map(int, input().split())

b = math.log(K, 2)
t = 0
for i in range(1, N + 1):
  if i >= K:
    t += 1 / N
    continue

  p = b - math.log(i, 2)
  p = math.ceil(p)

  t += 1 / N * ((1 / 2) ** p)

  # print(i, p)
print(t)