#!/usr/bin/env python3
N, M, X, T, D = map(int, input().split())

heights = [0] * (N + 1)

heights[N] = T
for i in range(N, 0, -1):
  if i > X:
    heights[i - 1] = heights[i]
  else:
    heights[i - 1] = heights[i] - D

print(heights[M])