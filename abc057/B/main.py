#!/usr/bin/env python3.8
N, M = map(int, input().split())
ps = []
for i in range(N):
  a, b = map(int, input().split())
  ps.append((a, b))

qs = []
for i in range(M):
  c, d = map(int, input().split())
  qs.append((c, d))

for p in ps:
  min_d = 9999999999999999999
  min_j = None
  for j, q in enumerate(qs, 1):
    m = abs(p[0] - q[0]) + abs(p[1] - q[1])
    if min_d > m:
      min_d = m
      min_j = j
  print(min_j)