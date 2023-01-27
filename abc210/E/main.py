#!/usr/bin/env python3.8
# https://note.nkmk.me/python-union-find/
from math import gcd

N,M=map(int, input().split())
edges = []
for i in range(M):
  a,c=map(int, input().split())
  edges.append((c, a))

edges.sort()

tot = 0
xx = N
g = N
for edge in edges:
  c, a = edge
  g = gcd(a, g)
  tot += (xx - g) * c
  xx = g

# print('xx', xx)
if xx <= 1:
  print(tot)
else:
  print(-1)