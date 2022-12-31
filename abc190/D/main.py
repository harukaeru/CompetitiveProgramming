#!/usr/bin/env pypy3
# 素因数分解
import math

N = int(input())
N *= 2
ma = int(math.sqrt(N))

fact = set()
for i in range(1, ma + 1):
  if N % i == 0:
    fact.add(i)
    fact.add(N // i)

cnt = 0
for n in fact:
  p = N // n - n + 1
  if p % 2 == 0:
    cnt += 1

print(cnt)