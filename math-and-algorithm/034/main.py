#!/usr/bin/env python3.8
import math
N = int(input())
A = []
for i in range(N):
  x, y = map(int, input().split())
  A.append((x, y))

min_d = 99999999999999
for i in range(N - 1):
  a_i = A[i]
  for j in range(i + 1, N):
    a_j = A[j]
    min_d = min(min_d, math.sqrt((a_i[0] - a_j[0]) ** 2 + (a_i[1] - a_j[1]) ** 2))

print(min_d)