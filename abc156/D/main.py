#!/usr/bin/env pypy3

mod = 10**9+7

def cmb(n, a):
  dn = n
  x = 1
  for i in range(a):
    x *= dn
    x %= mod
    dn -= 1

  y = 1
  for i in range(1, a + 1):
    y *= i
    y %= mod
  
  q = x * pow(y, mod - 2, mod) % mod
  return q

n,a,b = map(int, input().split())

tot = pow(2, n, mod) - 1

# print('tot', tot)
tot -= cmb(n,a)
tot -= cmb(n,b)
print(tot % mod)