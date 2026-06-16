#!/usr/bin/env python3.8
N = int(input())
keys = []
for i in range(N):
  P = list(map(int, input().split()))
  key = (sum(P), P[0], P[1])
  keys.append(key)

keys.sort()
minX = N
minY = N

count = 0
for key in keys:
  if key[1] <= minX:
    minX = key[1]
    count += 1
    if key[2] <= minY:
      minY = key[2]
  elif key[2] <= minY:
    minY = key[2]
    count += 1
print(count)