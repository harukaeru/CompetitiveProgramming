#!/usr/bin/env python3
N, X, Y = map(int, input().split())
reds = [0] * (N + 1)
blues = [0] * (N + 1)
reds[N] = 1

for n in range(N, 1, -1):
  reds[n - 1] += reds[n]
  blues[n] += reds[n] * X

  blues[n - 1] = blues[n] * Y
  reds[n - 1] += blues[n]

print(blues[1])