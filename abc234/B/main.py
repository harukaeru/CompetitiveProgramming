#!/usr/bin/env python3
import math

N = int(input())
coordinates = []
for i in range(N):
  coordinates.append(tuple(map(int, input().split())))

max_s = -1
for i in range(N):
  a = coordinates[i]
  for j in range(i + 1, N):
    b = coordinates[j]

    dx = a[0] - b[0]
    dy = a[1] - b[1]
    s = math.sqrt(dx * dx + dy * dy)
    max_s = max(max_s, s)

print(max_s)