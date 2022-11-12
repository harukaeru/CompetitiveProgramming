#!/usr/bin/env python3.8
W, H, N = map(int, input().split())

rightmost = W
leftmost = 0
top = H
bottom = 0
for i in range(N):
  x, y, a = map(int, input().split())
  if a == 1:
    leftmost = max(leftmost, x)
  elif a == 2:
    rightmost = min(rightmost, x)
  elif a == 3:
    bottom = max(bottom, y)
  else:
    top = min(top, y)

print(max(rightmost - leftmost, 0) * max(top - bottom, 0))