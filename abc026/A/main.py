#!/usr/bin/env python3.8
A = int(input())

m = -1
for i in range(1, 101):
  for j in range(1, 101):
    if i + j == A:
      m = max(m, i * j)

print(m)