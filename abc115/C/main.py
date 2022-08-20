#!/usr/bin/env python3
N, K = map(int, input().split())
hs = []
for i in range(N):
  hs.append(int(input()))

hs.sort()

ds = []
for i in range(len(hs) - K + 1):
  d = hs[i + K - 1] - hs[i] 
  ds.append(d)

print(min(ds))