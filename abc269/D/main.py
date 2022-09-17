#!/usr/bin/env python3
from collections import defaultdict

N = int(input())
XY = []
for i in range(N):
  x, y = map(int, input().split())
  XY.append((x, y))

directions = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]
seen = set()
dests = set(XY)
g = 0

q = []
for (a, b) in XY:
  if (a, b) in seen:
    continue

  q.append((a, b))
  g += 1
  while len(q) > 0:
    x, y = q.pop()
    if (x, y) not in seen:
      seen.add((x, y))

    for d in directions:
      dest = (x + d[0], y + d[1])
      if dest in dests and dest not in seen:
        q.append(dest)

print(g) 