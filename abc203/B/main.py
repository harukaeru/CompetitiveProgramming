#!/usr/bin/env python3.8
N, K = map(int, input().split())

r = 0
for i_seed in range(N):
  i = i_seed + 1
  for j_seed in range(K):
    j = j_seed + 1
    r += i * 100 + j

print(r)
