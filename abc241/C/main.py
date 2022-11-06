#!/usr/bin/env python3.8
N = int(input())
S = []
for i in range(N):
  S.append(input())

directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

def check(S, pos, dr):
  cnt = 0
  for i in range(6):
    lx = pos[0] + dr[0] * i
    ly = pos[1] + dr[1] * i
    if lx < 0 or lx > N - 1 or ly < 0 or ly > N - 1:
      return False

    cnt += S[lx][ly] == '#'
  return cnt >= 4

for i in range(N):
  for j in range(N):
    for dr in directions:
      if check(S, (i, j), dr):
        print('Yes')
        exit()

print('No')