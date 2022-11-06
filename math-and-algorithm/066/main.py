#!/usr/bin/env python3.8
N, K = map(int, input().split())

cnt = 0
for b in range(1, N + 1):
  for w in range(max(1, b - (K - 1)), min(b + K - 1, N) + 1):
    for g in range(max(1, b - (K - 1)), min(b + K - 1, N) + 1):
      if abs(w - g) < K:
        cnt += 1

print(N ** 3 - cnt)