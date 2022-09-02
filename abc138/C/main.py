#!/usr/bin/env python3
N = int(input())
v = [a for a in map(int, input().split())]

v.sort()

value = (v[1] + v[0]) / 2
for i in range(2, N):
  value = (value + v[i]) / 2

print(value)
