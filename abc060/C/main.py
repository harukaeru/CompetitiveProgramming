#!/usr/bin/env python3.8
N, T = map(int, input().split())
times = list(map(int, input().split()))

s = 0
for i in range(N - 1):
  t = times[i]
  nt = min(t + T, times[i + 1])
  d = nt - t
  s += d

s += T
print(s)