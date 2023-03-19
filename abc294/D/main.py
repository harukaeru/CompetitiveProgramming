#!/usr/bin/env pypy3
from collections import deque
import heapq


N,Q=map(int, input().split())

queue = deque(list(range(1, N + 1)))
called = []
came_people = set()

for i in range(Q):
  event = list(map(int, input().split()))
  if event[0] == 1: 
    v = queue.popleft()
    heapq.heappush(called, v)
  if event[0] == 2: 
    v = event[1]
    came_people.add(v)
  if event[0] == 3: 
    while 1:
      v = heapq.heappop(called)
      if v not in came_people:
        print(v)
        heapq.heappush(called, v)
        break
