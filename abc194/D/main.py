#!/usr/bin/env pypy3
N = int(input())

e = 0
for i in range(1, N):
  e += N / (N - i)
print(e)