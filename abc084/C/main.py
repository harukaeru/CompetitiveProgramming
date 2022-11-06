#!/usr/bin/env python3.8
import math
N = int(input())

vec = []
for i in range(N - 1):
  vec.append(list(map(int, input().split())))

result = []
for i in range(N):
  t = 0
  for j, (c, s, f) in enumerate(vec[i:]):
    if s >= t:
      t = s
    else:
      n = int((t - s - 0.0001) // f)
      next_dep = s + (n + 1) * f
      t = next_dep

    t += c
  result.append(t)

for r in result:
  print(r)