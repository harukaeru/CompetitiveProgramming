#!/usr/bin/env python3.8
from collections import deque, defaultdict
h, w = map(int, input().split())

M = []
black_cnt = 0
for i in range(h):
  m = input()
  M.append(m)
  black_cnt += m.count('#')

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dist = defaultdict(int)
seen = set()

q = deque()
q.append((0, 0))
seen.add((0, 0))
dist[(0, 0)] = 0
while len(q) > 0:
  i, j = q.popleft()

  for dr in directions:
    ni = i + dr[0]
    nj = j + dr[1]
    if 0 <= ni <= h - 1 and 0 <= nj <= w - 1:
      if (ni, nj) not in seen and M[ni][nj] == '.':
        dist[(ni, nj)] = dist[(i, j)] + 1
        seen.add((ni, nj))
        q.append((ni, nj))

last = (h - 1, w - 1)
if last not in seen:
  print(-1)
  exit()

# 全体 - すでに塗ってある数 - ぬれない数[距離+1]
print(h * w - black_cnt - (dist[last] + 1))


# seen = set()
# q = deque()
# last = (h - 1, w - 1)
# q.append(last)
# seen.add(last)
# replays = [last]
# while len(q) > 0:
#   i, j = q.popleft()
# 
#   for dr in directions:
#     ni = i + dr[0]
#     nj = j + dr[1]
#     if 0 <= ni <= h - 1 and 0 <= nj <= w - 1:
#       if (ni, nj) not in seen and M[ni][nj] == '.':
#         if dist[(i, j)] - 1 == dist[(ni, nj)]:
#           replays.append((ni, nj))
#           q.append((ni, nj))
#         seen.add((ni, nj))
# 
# print(dist)
# replays.reverse()
# print(replays)