#!/usr/bin/env python3.8
import math
MOD = 1000000007
X, Y = map(int, input().split())

m = max(X, Y)
w = min(X, Y)

u = 1
for i in range(X + Y, m, -1):
  u *= i
  u %= MOD

def modinv(x):
  p = MOD - 2
  y = x
  ans = 1
  for i in range(31):
    if (p & (1 << i)) != 0:
      ans *= y
      ans %= MOD
    y *= y
    y %= MOD
  return ans

for j in range(1, w + 1):
  inv = modinv(j)
  u *= inv
  u %= MOD

print(u)
# print(math.comb(X + Y, X) % MOD)

