#!/usr/bin/env python3.8
N, K, Q = map(int, input().split())

counter = [0] * N
for i in range(Q):
  A = int(input())
  counter[A - 1] += 1

for i, c in enumerate(counter):
  if K - (Q - c) > 0:
    print('Yes')
  else:
    print('No')