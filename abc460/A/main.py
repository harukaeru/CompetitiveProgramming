#!/usr/bin/env python3.8
N, M = list(map(int, input().split()))

cnt = 0
while M > 0:
  M = N % M
  cnt += 1

print(cnt)