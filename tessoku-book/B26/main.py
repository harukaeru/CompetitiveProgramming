#!/usr/bin/env python3.8
import math

N = int(input())

P = [0] * (N + 1)
P[0] = 1
P[1] = 1

M = int(math.sqrt(N)) + 1
for i in range(2, M):
  for j in range(i * 2, N + 1, i):
    P[j] = 1

for i in range(N + 1):
  if P[i] == 0:
    print(i)