#!/usr/bin/env python3
import math
from collections import deque, defaultdict
N = int(input())
sx, sy, tx, ty = map(int, input().split())
xys = []
rs = []
for i in range(N):
  x, y, r = map(int, input().split())
  xys.append((x, y))
  rs.append(r)

def get_intersections(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    d = (x1-x0)**2 + (y1-y0)**2
    
    # non intersecting
    if d > (r0 + r1) * (r0 + r1):
        return None
    # One circle within other
    if d < abs(r0-r1) * abs(r0 - r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
      return True

G = defaultdict(list)
for i in range(N - 1):
  for j in range(i + 1, N):
    a, b = xys[i]
    c, d = xys[j]
    r = rs[i]
    q = rs[j]
    intersections = get_intersections(a, b, r, c, d, q)
    if intersections:
      G[i].append(j)
      G[j].append(i)

def has_point(kx, ky, ci):
  x, y = xys[ci]
  r = rs[ci]
  p = (kx - x)
  q = (ky - y)

  # 円上に存在
  if p * p + q * q == r * r:
    return True
  return False

starts = []
for i in range(N):
  if has_point(sx, sy, i):
    starts.append(i)

ends = set()
for i in range(N):
  if has_point(tx, ty, i):
    ends.add(i)
# print('starts', starts)
# print('ends', ends)

q = deque(starts)
seen = set(starts)

while len(q) > 0:
  st = q.popleft()
  if st in ends:
    print('Yes')
    exit()

  for n in G[st]:
    if n not in seen:
      seen.add(n)
      q.append(n)

print('No')
