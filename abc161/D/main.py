#!/usr/bin/env python3.8
from collections import deque

K = int(input())

q = deque()
for i in [1, 2, 3, 4, 5, 6 ,7, 8, 9]:
  q.append(i)

for i in range(K):
  v = q.popleft()
  bottom = v % 10
  if bottom == 0:
    q.append(v * 10)
    q.append(v * 10 + 1)
  elif bottom == 9:
    q.append(v * 10 + 8)
    q.append(v * 10 + 9)
  else:
    q.append(v * 10 + bottom - 1)
    q.append(v * 10 + bottom)
    q.append(v * 10 + bottom + 1)
print(v)