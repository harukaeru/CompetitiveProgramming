#!/usr/bin/env python3
from queue import deque
N = int(input())
A = []
for i in range(N):
  a = [int(s) for s in input()]
  A.append(a)

directions = [
  (-1, 1),
  (0, 1),
  (1, 1),
  (-1, 0),
  (1, 0),
  (-1, -1),
  (0, -1),
  (1, -1),
]

max_data = 0
for i in range(N):
  for j in range(N):
    x, y = i, j

    for d in directions:
      data = 0
      for k in range(N):
        data *= 10
        data += A[x][y]
        x = (x + d[0] + N) % N
        y = (y + d[1] + N) % N
      max_data = max(max_data, data)
    
print(max_data)