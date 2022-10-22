#!/usr/bin/env pypy3
from collections import deque
N, x, y = map(int, input().split())
A = list(map(int, input().split()))

M = 10001

dp = []
for i in range(N):
  d = []
  xs = [False] * (2 * M + 1)
  ys = [False] * (2 * M + 1)
  d.append(xs)
  d.append(ys)
  dp.append(d)

XX = 0
YY = 1
dp[0][XX][M + A[0]] = True
dp[0][YY][M] = True

for i in range(1, N):
  a = A[i]
  target = YY if i % 2 == 1 else XX
  non_target = XX if i % 2 == 1 else YY

  for ci, q in enumerate(dp[i - 1][target]):
    if ci + a < 2 * M + 1:
      dp[i][target][ci + a] |= dp[i - 1][target][ci]

    if 0 <= ci - a:
      dp[i][target][ci - a] |= dp[i - 1][target][ci]
  dp[i][non_target] = dp[i - 1][non_target]

# print(dp[N - 1]['x'])
# print(dp[N - 1]['y'])

if dp[N - 1][XX][x + M] and dp[N - 1][YY][y + M]:
  print('Yes')
else:
  print('No')
# for d in dp:
#   print('x', d['x'])
#   for i, xx in enumerate(d['x']):
#     if xx:
#       print(i - M, end=' ')
#   print()
#   print('y', d['y'])
#   for i, xx in enumerate(d['y']):
#     if xx:
#       print(i - M, end=' ')
#   print()
#   print('-------')
