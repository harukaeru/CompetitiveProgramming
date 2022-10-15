#!/usr/bin/env python3
from collections import deque
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

HW = []
for i in range(R):
  HW.append(input())

INF = 99999999999
dists = []
for i in range(R):
  dists.append([INF] * C)
dists[sy][sx] = 0

q = deque()
q.append((sy, sx))

while len(q) > 0:
  y, x = q.popleft()
  if y == gy and x == gx:
    print(dists[y][x])
    exit()
  for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    if x + dx < 0 or C <= x + dx:
      continue
    if y + dy < 0 or R <= y + dy:
      continue

    if HW[y + dy][x + dx] == '.' and dists[y + dy][x + dx] == INF:
      dists[y + dy][x + dx] = dists[y][x] + 1
      q.append((y + dy, x + dx))