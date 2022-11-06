#!/usr/bin/env python3.8
N = int(input())

s = 0
for i in range(N):
  s += N / (N - i)

print(s)