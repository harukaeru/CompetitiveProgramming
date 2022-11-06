#!/usr/bin/env python3.8
N = int(input())
H = list(map(int, input().split()))

current = -1
for h in H:
  if current < h:
    current = h
  else:
    break
print(current)
