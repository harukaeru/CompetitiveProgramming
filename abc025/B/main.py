#!/usr/bin/env python3.8
N, A, B = map(int, input().split())
tot = 0
for i in range(N):
  s, d = input().split()
  d = int(d)
  d = min(max(d, A), B)
  if s == 'East':
    tot += d
  else:
    tot -= d


if tot > 0:
  print('East', tot)
elif tot < 0:
  print('West', -tot)
else:
  print(0)