#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

cnt = 0
bugs = 0
for a in A:
  if a != 0:
    cnt += 1
    bugs += a

print((bugs + cnt - 1)// cnt)
