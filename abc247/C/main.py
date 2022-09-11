#!/usr/bin/env python3
N = int(input())

S = [1]
for i in range(1, N):
  k = i + 1
  S = S + [k] + S

print(' '.join(map(str, S)))