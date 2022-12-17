#!/usr/bin/env python3.8
K = int(input())

s = ''
for i in range(ord('A'), ord('A') + K):
  s += chr(i)
print(s)