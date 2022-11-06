#!/usr/bin/env python3.8
import math
N, K = map(int, input().split())
V = list(map(int, input().split()))

s = 0
for i in range(K):
  lcm = 1
  cnt = 0
  for v in V[:i]:
    lcm = lcm * V[i] // math.gcd(lcm, V[i])
  if i % 2 == 0:
    s += N // lcm
  else:
    s -= N // lcm

print(s)
