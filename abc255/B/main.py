#!/usr/bin/env python3
import math
N, K = map(int, input().split())
A = list(map(int, input().split()))

lights = set(A)

points = []
for i in range(N):
  x, y = map(int, input().split())
  points.append((x, y))

closest_distance_list = []
for i in range(N):
  if i + 1 in lights:
    continue

  min_d_2 = 99999999999999
  point = points[i]
  for a in A:
    light = points[a - 1]

    dx = light[0] - point[0]
    dy = light[1] - point[1]
    d_2 = dx * dx + dy * dy
    min_d_2 = min(min_d_2, d_2)
  closest_distance_list.append(min_d_2)

required_r_2 = max(closest_distance_list)

print(math.sqrt(required_r_2))