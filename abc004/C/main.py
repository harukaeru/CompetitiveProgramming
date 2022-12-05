#!/usr/bin/env python3.8
N = int(input())

N %= 30

x = ['1', '2', '3', '4', '5', '6']
for i in range(N):
  x[(i % 5)], x[(i % 5) + 1] = x[(i % 5) + 1], x[(i % 5)]

print(''.join(x))
