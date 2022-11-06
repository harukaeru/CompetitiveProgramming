#!/usr/bin/env python3.8
class RMQ:
  INF = 2 ** 31 - 1
  def __init__(self, data):
    size = len(data)
    # p = math.ceil(math.log(size, 2))
    n = 1
    while n < size:
      n *= 2
    self.n = n
    self.nodes = [RMQ.INF] * (2 * n - 1)

    for i in range(size):
      # いちばん底のnodeたち
      self.nodes[(n - 1) + i] = data[i]
    
    for i in range(n - 2, -1, -1):
      self.nodes[i] = min(self.nodes[2 * i + 1], self.nodes[2 * i + 2])
    
  def update(self, pos, val):
    pos = (self.n - 1) + pos
    self.nodes[pos] = val
    while pos > 0:
      pos = (pos - 1) // 2
      self.nodes[pos] = min(self.nodes[2 * pos + 1], self.nodes[2 * pos + 2])
  
  def query(self, a, b):
    return self._query(a, b, 0, 0, self.n)

  def _query(self, a, b, k, l, r):
    if r <= a or b <= l:
      return RMQ.INF
    
    if a <= l and r <= b:
      return self.nodes[k]

    left = self._query(a, b, 2 * k + 1, l, (l + r) // 2)
    right = self._query(a, b, 2 * k + 2, (l + r) // 2, r) 
    return min(left, right)

n, q = map(int, input().split())
A = [2 ** 31 - 1] * n
# import math
# def print_rmq(rmq):
#   print('--------')
#   rep = 1
#   while rep < n:
#     rep *= 2
# 
#   k = 0
#   for i in range(rep):
#     next_k = 2 * k + 1
#     print(rmq.nodes[k:next_k])
#     k = next_k

rmq = RMQ(A)
for j in range(q):
  command, i, v = map(int, input().split())
  if command == 0:
    rmq.update(i, v)
    # print_rmq(rmq)

  else:
    x, y = i, v + 1
    print(rmq.query(x, y))