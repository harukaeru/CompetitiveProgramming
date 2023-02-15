#!/usr/bin/env python3.8
from collections import deque


H,W=map(int, input().split())
C = []
for i in range(H):
  c = input()
  C.append(c)

dp = []
for i in range(H):
  d = [0] * W
  dp.append(d)

dp[0][0] = 1
q = deque()
q.append((0, 0))

directions = [(1, 0), (0, 1)]

checked = set()
while len(q) > 0:
  v = q.popleft()
  if v in checked:
    continue
  checked.add(v)

  y,x = v
  # print('y,x', (y, x))

  for dx, dy in directions:
    if y + dy >= H:
      continue
    if x + dx >= W:
      continue
    
    if C[y + dy][x + dx] == '#':
      continue

    dp[y + dy][x + dx] += dp[y][x]
    q.append((y + dy, x + dx))

print(dp[H - 1][W - 1])