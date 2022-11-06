#!/usr/bin/env python3.8
from collections import deque
N = int(input())
S = input()


q = deque()
q.append(N)

for i in range(N - 1, -1, -1):
  s = S[i]
  if s == 'L':
    q.append(i)
  else:
    q.appendleft(i)

print(*q)