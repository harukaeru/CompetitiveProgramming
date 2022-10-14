#!/usr/bin/env python3
from queue import deque

class Queue:
  def __init__(self):
    self.que = deque()

  def append(self, x, c):
    self.que.append((x, c))

  def pop(self, c):
    tot = 0
    while 1:
      x, qc = self.que.popleft()
      if c < qc:
        self.que.appendleft((x, qc - c))
        tot += x * c
        break
      elif c == qc:
        tot += x * c
        break
      else:
        tot += x * qc
        c -= qc
        continue
    # print(self.que)
    return tot

que = Queue()
Q = int(input())
for i in range(Q):
  q, *p = map(int, input().split())
  if q == 1:
    x, c = p
    que.append(x, c)
  else:
    c = p[0]
    tot = que.pop(c)
    print(tot)