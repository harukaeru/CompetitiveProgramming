#!/usr/bin/env python3.8
from collections import deque


H,W=list(map(int,input().split()))
C = []
for i in range(H):
  row = list(input())
  C.append(row)

q = deque()
ans = [0] * min(H, W)

seen = set()

for i in range(H):
  for j in range(W):
    if C[i][j] == '.':
      continue

    if (i, j) in seen:
      continue

    q.append([(i, j), 1])
    # print((i, j))
    size = 1
    while len(q) > 0:
      v, s = q.popleft()
      seen.add((v[0], v[1]))

      downright = [v[0] + 1, v[1] + 1]

      if downright[0] >= H or downright[1] >= W or C[downright[0]][downright[1]] == '.':
        break
      # print('  down ', downright)

      size = s + 1
      q.append([downright, size])

    size //= 2
    if size == 0:
      continue
    # print((i, j), size)
    ans[size - 1] += 1

print(*ans)

