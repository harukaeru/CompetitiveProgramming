#!/usr/bin/env pypy3
from itertools import permutations
N = int(input())

# x = lambda: datetime.datetime.now()
# n = x()

A = {}
for i in range(2 * N - 1):
  a = list(map(int, input().split()))
  for j, v in enumerate(a):
    A[(i + 1, i + j + 2)] = v
    A[(i + j + 2, i + 1)] = v

q = list(range(1, 2 * N + 1))

# print('s1', x() - n)

used = [False] * (2 * N)

mb = -1
b = 0
def dfs():
  global b
  global mb
  l = None
  for i in range(2 * N):
    if not used[i]:
      used[i] = True
      l = i
      break

  for i in range(2 * N):
    if not used[i]:
      used[i] = True
      tmp = b
      b ^= A[(l + 1, i + 1)]
      # print((l+1,i+1))
      mb = max(mb, dfs())
      b = tmp
      used[i] = False
  if l is None:
    return b

  used[l] = False
  return mb

dfs()
print(mb)