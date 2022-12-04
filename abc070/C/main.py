#!/usr/bin/env python3.8
import math


N = int(input())
T = []
for i in range(N):
  t = int(input())
  T.append(t)

x = 1
for i in range(N):
  t = T[i]
  x = (t * x) // math.gcd(t, x)
print(x)