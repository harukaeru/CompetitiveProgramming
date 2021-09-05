#!/usr/bin/env python3
N = int(input())
*P, = map(int, input().split())

Q = [None] * N

for i in range(N):
    Q[P[i] - 1] = i + 1

print(' '.join(map(str, Q)))
