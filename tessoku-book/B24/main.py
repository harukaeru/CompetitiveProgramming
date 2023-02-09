#!/usr/bin/env python3.8
from bisect import bisect_left

N = int(input())
boxes = []
for i in range(N):
  x,y=map(int, input().split())
  boxes.append((x,y))

boxes.sort(key=lambda v: (v[0], -v[1]))

print(boxes)
ys = [v[1] for v in boxes]
# print(ys)

L = [1e18] * N

ml = 0
for i in range(N):
  pos = bisect_left(L, ys[i])
  L[pos] = min(L[pos], ys[i])
  ml = max(ml, pos + 1)

print('L', L)
print(ml)