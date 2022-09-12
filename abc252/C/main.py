#!/usr/bin/env python3
N = int(input())
S = []
for i in range(N):
  S.append(input())

min_tot = 999999
for t in range(10):
  tot = 0
  positions = [0] * 10
  for s in S:
    pos = s.index(str(t))
    val = 10 * positions[pos] + pos
    tot = max(val, tot)
    positions[pos] += 1
  min_tot = min(min_tot, tot)

print(min_tot)