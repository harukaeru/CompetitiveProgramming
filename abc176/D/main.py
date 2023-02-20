#!/usr/bin/env python3.8
from collections import defaultdict, deque


H,W=map(int, input().split())
ch,cw=map(int, input().split())
dh,dw=map(int, input().split())

DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

S = []
for i in range(H):
  s = input()
  S.append(s)

q = deque()
types = []
for i in range(H):
  t = [None] * W
  types.append(t)

typ = 0
for i in range(H):
  for j in range(W):
    if S[i][j] != '#' and types[i][j] is None:
      typ += 1
      q.append((i, j))
      types[i][j] = typ

      while len(q) > 0:
        y, x = q.popleft()
        for dy, dx in DIRECTIONS:
          ny = y + dy
          nx = x + dx
          if nx < 0 or nx >= W or ny < 0 or ny >= H:
            continue
          if S[ny][nx] == '#':
            continue
          if types[ny][nx] is None:
            types[ny][nx] = types[y][x]
            q.append((ny, nx))


G = defaultdict(set)

for i in range(H):
  for j in range(W):
    if S[i][j] != '#' and types[i][j] is not None:
      current_typ = types[i][j]
      for dy in range(-2, 3):
        for dx in range(-2, 3):
          ny = i + dy
          nx = j + dx
          if nx < 0 or nx >= W or ny < 0 or ny >= H:
            continue
          if types[ny][nx] is None:
            continue
          if types[ny][nx] != current_typ:
            # if ny == 0 and nx == 1:
            #   print('dy,dx', dy,dx)
            #   print('types[ny][nx]', ny, nx, types[ny][nx])
            #   print(current_typ)
            #   print(i, j)
            G[current_typ].add(types[ny][nx])
            G[types[ny][nx]].add(current_typ)

          
start = types[ch-1][cw-1]
goal = types[dh-1][dw-1]
q = deque()
q.append(start)
dists = [1e18] * (H * W)
dists[start] = 0

while q:
  v = q.popleft()
  for nex in G[v]:
    if dists[nex] != 1e18:
      continue
    dists[nex] = dists[v] + 1
    q.append(nex)

ans = dists[goal]
if ans == 1e18:
  print(-1)
else:
  print(ans)