#!/usr/bin/env python3
N = int(input())
MOD = 1000000007

def modpow(p, n):
  y = p
  ans = 1
  for i in range(60):
    if (n & (1 << i)) != 0:
      ans *= y
      ans %= MOD
    y *= y
    y %= MOD
  return ans

# def modinv(p):
#   k = MOD - 2
#   y = p
#   ans = 1
#   for i in range(31):
#     if (k & (1 << i)) != 0:
#       ans *= y
#       ans %= MOD
#     y *= y
#     y %= MOD
#   return ans

print((modpow(4, N + 1) - 1) * modpow(3, MOD - 2) % MOD)