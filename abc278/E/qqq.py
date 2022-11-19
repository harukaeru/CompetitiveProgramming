#!/usr/bin/env python3.8
import numpy
from collections import Counter

H, W, N, h, w = map(int, input().split())

HW = []
for i in range(H):
  HW.append(list(map(int, input().split())))

dp = []
for i in range(H):
  d = []
  for j in range(W):
    d.append(None)
  dp.append(d)

m = (H - 1) * (W - 1)
for p in range(m + 1):
  for i in range(p + 1):
    j = p - i
    if 0 <= i <= H - 1 and 0 <= j <= W - 1:
      nex = numpy.zeros(N)
      nex[H[i][j]] = 1
      if 0 <= i - 1:
        numpy.add(nex, dp[i - 1][j])
      if 0 <= j - 1:
        numpy.add(nex, dp[i][j - 1])
      if 0 <= i - 1 and 0 <= j - 1:
        numpy.subtract(nex, dp[i - 1][j - 1])
      
      dp[i][j] = nex
      # print('  ', i, j)

# print('dpppp')
# for d in dp:
#   print(d)
# 
# print('-------')

tot = dp[H - 1][W - 1]
# for i in range(H):
#   for j in range(W):
#     ro
# print('TOTAL', tot)
# for hw in HW:
#   print(hw)

for k in range(H - h + 1):
  a = []
  for l in range(W - w + 1):
    ex = numpy.zeros(N)
    if 0 <= k - 1:
      ex = numpy.add(ex, dp[k - 1][l + w - 1])
    if 0 <= l - 1:
      ex = numpy.add(ex, dp[k + h - 1][l - 1])
    if 0 <= k - 1 and 0 <= l - 1:
      ex = numpy.subtract(ex, dp[k - 1][l - 1])
    p = dp[k + h - 1][l + w - 1]
    pans = numpy.subtract(p, ex)
    ans = numpy.subtract(tot, p)
    l = numpy.count_nonzero(ans)
    a.append(l)
  print(*a)
