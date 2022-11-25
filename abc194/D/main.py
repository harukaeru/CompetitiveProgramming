#!/usr/bin/env pypy3
N = int(input())

v = 0
for N in range(1, 10000):
  e = 0
  for i in range(1, N):
    e += N / (N - i)
  if v < e // N:
    v = e // N
    print(N, ':', v, ':', e)