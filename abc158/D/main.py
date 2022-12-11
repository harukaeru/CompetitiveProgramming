#!/usr/bin/env python3.8
from collections import deque

S = input()
Q = int(input())

arr = deque(S)

dir = 1
for i in range(Q):
  q = input().split()
  if q[0] == '1':
    dir *= -1
  else:
    pos = None
    if q[1] == '1':
      pos = dir * 1
    else:
      pos = dir * -1

    if pos == 1:
      arr.appendleft(q[2])
    else:
      arr.append(q[2])

if dir == 1:
  print(''.join(arr))
else:
  print(''.join(reversed(arr)))