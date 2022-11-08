#!/usr/bin/env python3.8
from collections import deque
H, W = map(int, input().split())
C = []
dists = []
for i in range(H):
  C.append(input())
  dists.append([-1] * W)

q = deque()
q.append((0, 0))
dists[0][0] = 1

while len(q) > 0:
  y,x = q.popleft()
  for d in [(0, 1), (1, 0)]:
    ny, nx = y + d[0], x + d[1]
    if not (0 <= ny < H and 0 <= nx < W):
      continue

    if C[ny][nx] == '#':
      continue

    if dists[ny][nx] != -1:
      continue

    dists[ny][nx] = dists[y][x] + 1
    q.append((ny, nx))

print(max([max(d) for d in dists]))