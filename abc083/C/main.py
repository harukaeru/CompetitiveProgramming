#!/usr/bin/env python3
X, Y = map(int, input().split())

cnt = 0
while Y >= X:
  cnt += 1
  X *= 2

print(cnt)