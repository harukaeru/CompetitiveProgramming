#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

m = 0
cache = {}
def calc_production(d):
  if cache.get(d):
    return cache[d]

  tot = 0
  for i in range(d):
    tot += A[i // 2]
  cache[d] = tot
  return tot

dp = [-1e5] * (2 + N)

dp[1] = 0

for i in range(2, N + 2):
  for j in range(1, i):
    dp[i] = max(dp[i], dp[j] + calc_production(i - j - 1))

print(dp[N + 1])