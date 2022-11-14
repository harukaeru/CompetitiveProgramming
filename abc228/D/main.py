#!/usr/bin/env pypy3
import sys
sys.setrecursionlimit(300000000)
A = dict()
N = 2 ** 20
Q = int(input())
TX = []
for i in range(Q):
  t,x = map(int, input().split())
  TX.append((t,x))

parent = {}
def find(c):
  if parent.get(c % N, -1) == -1:
    parent[c % N] = (c + 1) % N
    return c % N
  last = find(parent[c % N])
  parent[c % N] = last
  return last

for i in range(Q):
  t,x = TX[i]

  if t == 1:
    h = x
    i = find(h)
    A[i] = x
  elif t == 2:
    print(A.get(x % N, -1))