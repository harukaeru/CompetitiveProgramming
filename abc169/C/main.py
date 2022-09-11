#!/usr/bin/env python3
A, B = input().split()

A = int(A)
b = B.split('.')
x = 0
if len(b) > 1:
  x += 100 * int(b[0])
  if len(b[1]) == 2:
    x += 10 * int(b[1][0])
    x += int(b[1][1])
  else:
    x += 10 * int(b[1][1])
else:
  x = 100 * int(b[0])

print(int(A) * x // 100)