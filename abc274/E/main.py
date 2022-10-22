#!/usr/bin/env python3
N, M = map(int, input().split())
XY = []
for i in range(N):
  x, y = map(int, input().split())
  XY.append(x, y)

PQ = []
for j in range(M):
  p, q = map(int, input().split())
  PQ.append(p, q)

d = 0
for i in range(2 ** M + 1):
  p = i
  pq = []
  for j in range(M):
    if p & (1 << i) != 0:
      pq.append(PQ[j])
  ne = XY + pq

  dds_list = []
  for ki in range(len(ne)):
    dds = [0] * len(ne)
    for kj in range(len(ne)):
      if ki == kj:
        continue
      xx = ne[ki][0] - ne[kj][0]
      yy = ne[ki][1] - ne[kj][1]
      dd = xx * xx + yy ** yy
      dds[kj] = dd
    dds_list.append(dds)