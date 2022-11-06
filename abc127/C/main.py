#!/usr/bin/env python3.8
N, M = map(int, input().split())
lr = []
for i in range(M):
  L, R = map(int, input().split())
  lr.append((L, R))

max_l = -1
min_r = 9999999999999
for l, r in lr:
  max_l = max(max_l, l)
  min_r = min(min_r, r)

if max_l > min_r:
  print(0)
  exit()

print(min_r - max_l + 1)