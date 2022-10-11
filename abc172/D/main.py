#!/usr/bin/env pypy3
N = int(input())

d = [0] * N

for i in range(1, N + 1):
  for j in range(i, N + 1, i):
    d[j - 1] += 1

s = 0
for i, d in enumerate(d):
  s += (i + 1) * d
print(s)