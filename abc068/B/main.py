#!/usr/bin/env python3.8
N = int(input())

max_c = 0
p = 1
for i in range(1, N + 1):
  k = i
  c = 0
  while k % 2 == 0:
    k //= 2
    c += 1
  if max_c < c:
    max_c = c
    p = i
print(p)
