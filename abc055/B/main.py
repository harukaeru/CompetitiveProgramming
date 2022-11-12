#!/usr/bin/env python3.8
N = int(input())

MOD = 10 **9 + 7
p = 1
for i in range(1, N + 1):
  p *= i
  p %= MOD

print(p)