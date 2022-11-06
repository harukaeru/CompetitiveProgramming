#!/usr/bin/env python3.8
H, W = map(int, input().split())
G = []
for i in range(H):
  G.append(input())

seen = set()
stack = []
stack.append((0, 0))
while len(stack) > 0:
  i, j = stack.pop()
  if (i, j) in seen:
    print(-1)
    exit()
  seen.add((i, j))

  if G[i][j] == 'U' and i != 0:
    stack.append((i - 1, j))
    continue
  if G[i][j] == 'D' and i != H - 1:
    stack.append((i + 1, j))
    continue
  if G[i][j] == 'L' and j != 0:
    stack.append((i, j - 1))
    continue
  if G[i][j] == 'R' and j != W - 1:
    stack.append((i, j + 1))
    continue

  print(*[i + 1, j + 1])