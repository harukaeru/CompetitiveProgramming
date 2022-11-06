#!/usr/bin/env python3.8
N = int(input())
P = list(map(int, input().split()))

current_min = 999999999999

cnt = 0
for i in range(N):
  if P[i] <= current_min:
    cnt += 1
  current_min = min(current_min, P[i])

print(cnt)