#!/usr/bin/env python3.8
import sys

N = int(input())
sys.setrecursionlimit(max(N, 10000))

times = []
reqs = []

got_skills = set()
got_skills.add(0)

for i in range(N):
  P = list(map(int, input().split()))
  t = P[0]
  times.append(t)

  k = P[1]
  A = P[2:]
  reqs.append(A)

stacks = []
stacks.append(N)

time = 0
while (len(stacks) > 0):
  idx = stacks.pop()
  if idx in got_skills:
    continue

  for prev_idx in reqs[idx - 1]:
    if prev_idx in got_skills:
      continue
    stacks.append(prev_idx)

  got_skills.add(idx)
  time += times[idx - 1]

print(time)