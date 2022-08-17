#!/usr/bin/env python3
import heapq
Q = int(input())

c = 0

class LeftHeap:
  def __init__(self):
    self.array = []
    self.total = 0
  
  def push(self, v):
    heapq.heappush(self.array, -v)
    self.total += v

  def top(self):
    v = heapq.heappop(self.array)
    heapq.heappush(self.array, v)
    return -v

  def pop(self):
    v = -heapq.heappop(self.array)
    self.total -= v
    return v

  def __len__(self):
    return len(self.array)

class RightHeap:
  def __init__(self):
    self.array = []
    self.total = 0
  
  def push(self, v):
    heapq.heappush(self.array, v)
    self.total += v

  def top(self):
    v = heapq.heappop(self.array)
    heapq.heappush(self.array, v)
    return v

  def pop(self):
    v = heapq.heappop(self.array)
    self.total -= v
    return v

  def __len__(self):
    return len(self.array)

L = LeftHeap()
R = RightHeap()

for i in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    a, b = query[1], query[2]

    if len(L) == 0:
      L.push(a)
    elif len(L) > len(R):
      median = L.top()
      if a >= median:
        R.push(a)
      else:
        L.pop()
        L.push(a)
        R.push(median)
    elif len(L) == len(R):
      median_large = R.top()
      if a <= median_large:
        L.push(a)
      else:
        R.pop()
        L.push(median_large)
        R.push(a)
    else:
      raise Exception()
    # print(L)
    # print(R)
    c += b
  else:
    median = L.top()
    ans = median * len(L) - L.total + R.total - median * len(R)
    print(median, ans + c)