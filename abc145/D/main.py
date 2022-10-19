#!/usr/bin/env pypy3
X, Y = map(int, input().split())
MOD = 10 ** 9 + 7

l = r = 0
for a in range(10 ** 6 + 1):
  b = X - 2 * a
  # print('a,b', a, b)
  if b < 0:
    continue
  if a + 2 * b == Y:
    l = a
    r = b
if l == r == 0:
  print(0)
  exit()

def modinv(r):
  k = MOD - 2
  y = r
  ans = 1
  for i in range(31):
    if (k & (1 << i)) != 0:
      ans *= y
      ans %= MOD
    y *= y
    y %= MOD
  return ans

def modcomb(n, r):
  x = 1
  for i in range(n, r, -1):
    x *= i
    x %= MOD

  for i in range(1, n - r + 1):
    mr = modinv(i)
    x *= mr
    x %= MOD
  return x
  

print(modcomb(l + r, r))