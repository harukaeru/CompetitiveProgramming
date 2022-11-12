#!/usr/bin/env python3.8
import math
N = int(input())
tot = 0
R = []
for i in range(N):
  r = int(input())
  R.append(r)

R.sort(reverse=True)
for i in range(N):
  r = R[i]
  s = r * r
  if i % 2 == 0:
    tot += s
  else:
    tot -= s

print(tot * math.pi)