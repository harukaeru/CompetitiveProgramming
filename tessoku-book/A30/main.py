#!/usr/bin/env python3.8
n,r=map(int, input().split())
mod = 1000000007

ne = 1
for i in range(n, 0, -1):
  ne *= i
  ne %= mod

re = 1
for i in range(r, 0, -1):
  re *= i
  re %= mod

nmre = 1
for i in range(n - r, 0, -1):
  nmre *= i
  nmre %= mod

print(ne * pow(re * nmre, mod - 2, mod) % mod)