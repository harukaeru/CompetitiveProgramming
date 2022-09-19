#!/usr/bin/env python3
N, W = map(int, input().split())

AB = []
for i in range(N):
  a, b = map(int, input().split())
  AB.append((a, b))

AB.sort()
AB.reverse()
d = 0
for a, b in AB:
  chosen_cnt = min(W, b)
  W -= chosen_cnt
  d += a * chosen_cnt

print(d)