#!/usr/bin/env python3.8
N = int(input())

d = 1
for i in range(1, N + 1):
  d *= i

print(d)