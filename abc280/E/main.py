#!/usr/bin/env python3.8
from collections import defaultdict


N, P = map(int, input().split())
MOD = 998244353

M = 10 ** 5

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

d = defaultdict(list)
d[0] = [(N, modinv(1))]

ps = []
i = 0
while 1:
  if not d[i]:
    break
  for x in d[i]:
    val, pa = x
    if val - 1 <= 0:
      ps.append(pa * P / 100)
    else:
      d[i + 1].append((val - 1, modinv(pa * P) / 100))

    if val - 2 <= 0:
      ps.append(pa * (100 - P) / 100)
    else:
      d[i + 1].append((val - 2, pa * (100 - P) / 100))
  i += 1
  

  print(d)
  print(ps)