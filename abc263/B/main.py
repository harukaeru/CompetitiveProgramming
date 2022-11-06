#!/usr/bin/env python3.8
N = int(input())
P = list(map(int, input().split()))

a = N
cnt = 0
while a != 1:
  a = P[a - 2]
  cnt += 1

print(cnt)