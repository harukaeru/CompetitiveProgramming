#!/usr/bin/env python3.8
from itertools import permutations
N, K = map(int, input().split())
T = []
for i in range(N):
  t = list(map(int, input().split()))
  T.append(t)

mids = list(range(1, N))

cnt = 0
for path in permutations(mids):
  current = 0
  time = 0
  for i, dest in enumerate(path):
    time += T[current][dest]
    current = dest
  time += T[current][0]

  if time == K:
    cnt += 1

print(cnt)
  