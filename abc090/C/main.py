#!/usr/bin/env python3
x = list(map(int, input().split()))
x.sort()
x = tuple(x)

if x == (1, 1):
  print(1)
  exit()

if x[0] == 1:
  print(x[1] - 2)
  exit()

print((x[0] - 2) * (x[1] - 2))
