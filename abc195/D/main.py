#!/usr/bin/env python3.8
from bisect import bisect_left


N, M, Q = map(int, input().split())
WV = []
for i in range(N):
  w, v = map(int, input().split())
  WV.append((w, -v))
WV.sort()

X = list(map(int, input().split()))
for i in range(Q):
  l, r = map(int, input().split())
  Y = X[:l-1] + X[r:]
  Y.sort()
  chosen_set = set()
  tot_value = 0
  for y in Y:
    pos = bisect_left(WV, (y, 1e18))
    maxv = 0
    chosen = None
    for i in range(pos):
      if i in chosen_set:
        continue
      if maxv < -WV[i][1]:
        maxv = -WV[i][1]
        chosen = i
    if chosen is not None:
      tot_value += maxv
      chosen_set.add(chosen)
  print(tot_value)