#!/usr/bin/env python3.8
N = int(input())
SP = []
tot = 0
for i in range(N):
  s, p = input().split()
  p = int(p)
  SP.append((s, p))
  tot += p

for sp in SP:
  if sp[1] > tot / 2:
    print(sp[0])
    exit()
print('atcoder')