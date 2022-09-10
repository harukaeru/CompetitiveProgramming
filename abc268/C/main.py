#!/usr/bin/env python3
N = int(input())
P = list(map(int, input().split()))

ranges = []
for i in range(N):
  humans = [(i - 1) % N, i % N, (i + 1) % N]
  ranges.append(humans)

rotates = []
for i in range(N):
  rot = []
  for human in ranges[i]:
    x = human - P[i]
    if x < 0:
      x = x + N
    rot.append(x)
  rotates.append(rot)

counter = {}
for rotate in rotates:
  counter.setdefault(rotate[0], 0)
  counter[rotate[0]] += 1
  counter.setdefault(rotate[1], 0)
  counter[rotate[1]] += 1
  counter.setdefault(rotate[2], 0)
  counter[rotate[2]] += 1

print(max(counter.values()))