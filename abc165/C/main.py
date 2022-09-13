#!/usr/bin/env python3
N, M, Q = map(int, input().split())

L = []
for i in range(Q):
  l = list(map(int, input().split()))
  L.append(l)

A = [list(range(1, M + 1)) for i in range(N)]

class Perm:
  def __init__(self, N, M):
    self.array = [1] * N
    self.N = N

  def plus(self, pos):
    if self.array[pos] < M:
      self.array[pos] += 1
    else:
      if pos == -1:
        raise ValueError
      self.plus(pos - 1)
      self.array[pos] = self.array[pos - 1]

max_point = 0
perm = Perm(N, M)
while 1:
  point = 0
  array = perm.array
  for a, b, c, d in L:
    if array[b - 1] - array[a - 1] == c:
      point += d

  max_point = max(max_point, point)
  try:
    perm.plus(N - 1)
  except ValueError:
    break

print(max_point)