#!/usr/bin/env python3
N, Q = map(int, input().split())

snows = [0] * (N + 1)

for i in range(Q):
  l, r, x = map(int, input().split())
  snows[l - 1] += x
  snows[r] -= x

dp = [0] * (N + 2)
for i in range(1, N + 1):
  dp[i] = dp[i - 1] + snows[i - 1]

ans = ''
for i in range(1, N):
  if dp[i] > dp[i + 1]:
    ans += '>'
  elif dp[i] == dp[i + 1]:
    ans += '='
  else:
    ans += '<'

print(ans)