#!/usr/bin/env python3.8
N, X, Y = map(int, input().split())

cnt = 0
for i in range(1, N + 1):
  if i % X == 0 or i % Y == 0:
    cnt += 1

print(cnt)