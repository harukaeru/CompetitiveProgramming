#!/usr/bin/env python3.8
import math
A, B, H, M = map(int, input().split())

h = 360 * H / 12 + 30 * M / 60
m = 360 * M / 60

deg = abs(h - m)

if deg == 0:
  print(abs(A - B))
elif deg == 180:
  print(abs(A + B))
else:
  print(math.sqrt(A * A + B * B - 2 * A * B * math.cos(math.radians(deg))))