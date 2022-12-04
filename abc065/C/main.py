#!/usr/bin/env python3.8
N, M = map(int, input().split())
MOD = 10 ** 9 + 7

if abs(N - M) > 1:
  print(0)
  exit()

A = max(N, M)
B = min(N, M)

ans = 1
for i in range(1, A + 1):
  ans *= i
  ans %= MOD

for i in range(1, B + 1):
  ans *= i
  ans %= MOD
if A == B:
  ans *= 2
  ans %= MOD
print(ans)