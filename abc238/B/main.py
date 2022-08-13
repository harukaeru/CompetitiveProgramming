#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))

t = 0
pos = [0, 360]
for a in A:
  t = (t + a) % 360
  pos.append(t)

pos.sort()

max_d = -1
for i in range(len(pos) - 1):
  d = pos[i + 1] - pos[i]
  max_d = max(max_d, d)


print(max_d)
