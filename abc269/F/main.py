#!/usr/bin/env python3.8
N, M = map(int, input().split())
Q = int(input())
mod = 998244353

S = []
for i in range(Q):
  a, b, c, d = map(int, input().split())
  S.append((a, b, c, d))

def sum(x, y):
  # print('x,y', x, y)
  k = 0
  k += sum2((x + 1) // 2, (y + 1) // 2, 1) % mod
  k += sum2(x // 2, y // 2, M + 2) % mod
  return k

def sum2(x, y, initial):
  s = initial
  e = initial + (x - 1) * 2 * M + (y - 1) * 2
  avg = (s + e) // 2
  count = x * y
  # print('------')
  # print('(x,y)', x, y)
  # print('e', e)
  # print('avg', avg)
  # print('count', count)
  # print('a', count * avg)
  return count * avg

for s in S:
  ans = 0
  a, b, c, d = s
  # print('-------------------')
  ans += sum(b, d)
  ans -= sum(a - 1, d)
  ans -= sum(b,  c - 1)
  ans += sum(a - 1, c - 1)
  print(ans % mod)