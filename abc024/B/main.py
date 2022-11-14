#!/usr/bin/env python3.8
N, T = map(int, input().split())
A = []
for i in range(N):
  A.append(int(input()))

tot = 0
cur = 0
for a in A:
  if cur != 0 and cur + T >= a:
    tot -= cur + T - a
  cur = a
  tot += T
print(tot)