#!/usr/bin/env python3.8
N = int(input())

s = 0
for i in range(1, 10):
  for j in range(1, 10):
    s += i * j

rest = s - N

for i in range(1, 10):
  for j in range(1, 10):
    if i * j == rest:
      print(i, 'x', j)
