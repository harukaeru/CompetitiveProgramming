#!/usr/bin/env pypy3
N = int(input())
MOD = 1000000007

a = 1
b = 1
for i in range(2, N):
  a, b = b, a + b
  b %= MOD

print(b)