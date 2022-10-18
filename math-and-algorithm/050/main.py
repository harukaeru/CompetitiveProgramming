#!/usr/bin/env pypy3
a, b = map(int, input().split())
MOD = 1000000007

ans = 1
p = a
for i in range(30):
  if (b & (1 << i)) != 0:
    ans *= p
    ans %= MOD
  p *= p
  p %= MOD

print(ans)
