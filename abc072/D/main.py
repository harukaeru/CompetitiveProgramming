#!/usr/bin/env python3.8
N = int(input())
P = list(map(int, input().split()))

cnt = 0
for i in range(1, N + 1):
  if i == N and i == P[i - 1]:
    P[i - 1], P[i - 2] = P[i - 2], P[i - 1]
    cnt += 1
  elif i == P[i - 1]:
    P[i - 1], P[i] = P[i], P[i - 1]
    cnt += 1
print(cnt)