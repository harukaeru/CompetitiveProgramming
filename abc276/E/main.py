#!/usr/bin/env pypy3
import sys
sys.setrecursionlimit(10**8)

H, W = map(int, input().split())
S = None
C = []
for i in range(H):
  st = input()
  C.append(st)
  try:
    st.index('S')
    S = (i, st.index('S'))
  except:
    pass


directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

seen = set()
seen.add(S)

def dfs(y, x, dis):
  # print((y, x), dis)

  for dir in directions:
    dy, dx = dir
    ny, nx = y + dy, x + dx
    if not (0 <= ny < H and 0 <= nx < W):
      continue

    c = C[ny][nx]

    if c == 'S' and dis >= 3:
      print('Yes')
      exit()
    if (ny, nx) in seen:
      continue

    if c == '#':
      continue

    seen.add((ny, nx))
    dfs(ny, nx, dis + 1)

dfs(S[0], S[1], 0)

print('No')