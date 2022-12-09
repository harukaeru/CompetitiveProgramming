#!/usr/bin/env python3.8
from collections import defaultdict


N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

score = 0
d = defaultdict(list)
for i in range(N):
  t = T[i]
  d[i % K].append(t)
# print(d)

tot = 0
for arr in d.values():
  score = 0
  cur = None
  for a in arr:
    if a == cur:
      cur = None
      continue
    if a == 'r':
      score += P
    elif a == 's':
      score += R
    else:
      score += S
    cur = a
  tot += score

print(tot)