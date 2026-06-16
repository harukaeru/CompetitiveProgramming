#!/usr/bin/env python3.8
N = int(input())
keys = []
for i in range(N):
  P = list(map(int, input().split()))
  key = (P[0], P[1])
  keys.append(key)

keys.sort()

count = 0
minY = N + 1
for key in keys:
    minY = min(key[1], minY)
    if minY == key[1]:
      count += 1
print(count)