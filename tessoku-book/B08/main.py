#!/usr/bin/env python3.8
from collections import Counter


N = int(input())
XY = []

counter = Counter()
my = 0
mx = 0
for i in range(N):
  x,y=map(int, input().split())
  counter[(y, x)] += 1
  my = max(my, y)
  mx = max(mx, x)

cache = []
for i in range(my + 1):
  cache.append([0] * (mx + 1))

for y in range(my):
  for x in range(mx):
    cache[y + 1][x + 1] = cache[y + 1][x] + cache[y][x + 1] - cache[y][x] + counter[(y + 1, x + 1)]


# for c in cache:
#   print(c)
# 
Q = int(input())
for i in range(Q):
  a,b,c,d = map(int, input().split())
  print(cache[d][c] - cache[d][a - 1] - cache[b - 1][c] + cache[b - 1][a - 1])