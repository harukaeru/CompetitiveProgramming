#!/usr/bin/env python3.8
from collections import defaultdict, deque
import math
S = []
for i in range(9):
  s = input()
  S.append(s)

G = []
for i in range(9):
  for j in range(9):
    if S[i][j] == '#':
      G.append((i, j))

sg = set(G)
cnt = 0
seen = set()
G.sort()
# print(G)
for g in G:
  for i in range(9):
    for j in range(9):
      if i == 0 and j == 0:
        continue
      directions = [(i, j), (j, -i), (-i, -j)]
      found = True
      cand = g
      # if g == (3, 7):
      #   print((i, j))
      #   print(directions)
      for d in directions:
        dx, dy = d
        cand = (cand[0] + dx, cand[1] + dy)
        if cand in seen:
          found = False
          break
        if cand not in sg:
          found = False
          break
      if found:
        # print(g)
        cnt += 1
  seen.add(g)
  # break
print(cnt) 