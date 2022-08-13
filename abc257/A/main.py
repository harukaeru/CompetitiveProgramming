#!/usr/bin/env python3
N, X = map(int, input().split())

s = ''
for i in range(ord('A'), ord('Z') + 1):
  s += chr(i) * N
print(s[X - 1])