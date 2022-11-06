#!/usr/bin/env python3.8
N = int(input())
h = list(map(int, input().split()))

cnt = 0
before = 0
for i in range(N):
  cnt += max(0, h[i] - before)
  before = h[i]

print(cnt)
