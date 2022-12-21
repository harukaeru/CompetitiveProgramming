#!/usr/bin/env python3.8
from collections import deque
import sys
sys.setrecursionlimit(3000000) 

H, W, A, B = map(int, input().split())

dists = []
for i in range(H):
  d = [0] * W
  dists.append(d)

nexes = ['small', 'big_y', 'big_x']

rest = {
  'big': A,
  'small': B
}

cnt = 0
def dfs(y, x, depth=0):
  # print('  ' * depth, (y, x))
  if all(all(d) for d in dists):
    # for d in dists:
    #   print(d)
    global cnt
    cnt += 1
    return

  if x == W:
    dfs(y + 1, 0, depth+1)
    return

  if dists[y][x] == 1:
    dfs(y, x + 1)
    return

  if y == H:
    return

  # small
  if dists[y][x] == 0 and rest['small'] > 0:
    dists[y][x] = 1
    rest['small'] -= 1
    dfs(y, x + 1, depth+1)
    rest['small'] += 1
    dists[y][x] = 0
  # big_y
  if y + 1 < H and dists[y][x] == 0 and dists[y + 1][x] == 0 and rest['big'] > 0:
    dists[y][x] = 1
    dists[y + 1][x] = 1
    rest['big'] -= 1
    dfs(y, x + 1, depth+1)
    rest['big'] += 1
    dists[y][x] = 0
    dists[y + 1][x] = 0
  # big_x
  if x + 1 < W and dists[y][x] == 0 and dists[y][x + 1] == 0 and rest['big'] > 0:
    dists[y][x] = 1
    dists[y][x + 1] = 1
    rest['big'] -= 1
    dfs(y, x + 2, depth+1)
    rest['big'] += 1
    dists[y][x] = 0
    dists[y][x + 1] = 0

dfs(0, 0, depth=0)
print(cnt)