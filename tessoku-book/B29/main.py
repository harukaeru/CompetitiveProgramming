#!/usr/bin/env python3.8
a,b=map(int, input().split())
mod = 1000000007

bb = bin(b)[2:]
ans = 1
p = a
for i in range(len(bb)):
  if (b & 1 << i) != 0:
    ans *= p
    ans %= mod
  p *= p
  p %= mod
print(ans)
