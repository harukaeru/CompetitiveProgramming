#!/usr/bin/env python3.8
from queue import deque
N, M = map(int, input().split())

dirs = []
for i in range(N):
  for j in range(N):
    if i * i + j * j == M:
      dirs.append((i, j))
      dirs.append((-i, j))
      dirs.append((-i, -j))
      dirs.append((i, -j))

dists = []
for i in range(N):
  d = [-1] * N
  dists.append(d)
dists[0][0] = 0

q = deque()
q.append((0, 0))
while len(q) > 0:
  x, y = q.popleft()

  for dir in dirs:
    next_pos = x + dir[0], y + dir[1]
    if next_pos[0] < 0 or next_pos[0] >= N:
      continue
    if next_pos[1] < 0 or next_pos[1] >= N:
      continue
    if dists[next_pos[0]][next_pos[1]] == -1:
      dists[next_pos[0]][next_pos[1]] = dists[x][y] + 1
      q.append(next_pos)

for d in dists:
  print(*d)