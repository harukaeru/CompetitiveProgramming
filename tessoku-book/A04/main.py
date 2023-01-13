#!/usr/bin/env python3.8
N = int(input())
L = []
for i in range(10):
  L.append(N % 2)
  N //= 2
L.reverse()
print(''.join(map(str, L)))