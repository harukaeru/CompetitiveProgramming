#!/usr/bin/env pypy3
from itertools import permutations
import math


N, M = map(int, input().split())
XY = []
for i in range(N):
  x, y = map(int, input().split())
  XY.append((x, y))

PQ = []
for j in range(M):
  p, q = map(int, input().split())
  PQ.append((p, q))

boosters = set(PQ)
T = [(0, 0)] + XY + PQ

dists = dict()

c = list(range(1, N + M + 1))
md = 9999999999999999
ps = list(permutations(c))
print('pscnt', len(ps))
for p in ps:
  q = (0,) + p
  denomi = 1
  tot_d = 0
  city_cnt = 0
  for i in range(len(q) - 1):
    x = T[q[i+1]][0] - T[q[i]][0]
    y = T[q[i+1]][1] - T[q[i]][1]
    d2 = x * x + y * y
    tot_d += math.sqrt(d2) / denomi
    if T[q[i + 1]] in boosters:
      denomi *= 2
    else:
      city_cnt += 1
    if city_cnt == N:
      x = T[q[i + 1]][0]
      y = T[q[i + 1]][1]
      d2 = x * x + y * y
      tot_d += math.sqrt(d2) / denomi
      break
  md = min(md, tot_d)
print(md)