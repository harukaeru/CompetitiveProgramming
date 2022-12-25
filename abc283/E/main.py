#!/usr/bin/env pypy3
from random import random


H, W = map(int, input().split())
A = []
for i in range(H):
  B = list(map(int, input().split()))
  A.append(B)

dp = []
for i in range(H + 1):
  d = []
  for j in range(2):
    e = [1e20, 1e20]
    d.append(e)
  dp.append(d)

dp[0][0][0] = 0
dp[0][0][1] = 1


def inverse(s):
  return [1 - x for x in s]


def check(i, rows):
  for j in range(W):
    ok = False
    for s in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
      if 0 <= i + s[0] < len(rows) and 0 <= j + s[1] < W:
        if rows[i][j] == rows[i + s[0]][j + s[1]]:
          ok = True
    if not ok:
      return False
  return True

cnt = 0
for i in range(1, H + 1):
  up = A[i - 2] if i != 1 else [-8] * W
  mid = A[i - 1]
  down = A[i] if i != H else [-8] * W
  for j in range(2):
    for k in range(2):
      for l in range(2):
        u = inverse(up) if j == 1 else up
        m = inverse(mid) if k == 1 else mid
        d = inverse(down) if l == 1 else down
        ok = check(1, [u, m, d])
        if ok:
          dp[i][k][l] = min(dp[i][k][l], dp[i - 1][j][k] + l)
          # print('  ', bool(j), bool(k), bool(down))
          # print('  ', u)
          # print('  ', m)
          # print('  ', d)
          # print('  ', ok)
          # print('  ', dp[i - 1])
          # print('  ', dp[i])

m = 1e19
# print(dp)
for d in dp[H]:
  m = min(m, min(d))

if m == 1e19:
  print(-1)
else:
  print(m)