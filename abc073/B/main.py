#!/usr/bin/env python3.8
N = int(input())
M = 100001
s = 0
for i in range(N):
  l, r = map(int, input().split())
  s += r - l + 1

print(s)