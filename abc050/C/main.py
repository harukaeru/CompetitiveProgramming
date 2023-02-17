#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

mod = 10 ** 9 + 7

dp = [0] * N

M = N - 1
for i in range(N):
  v = (M - A[i]) 
  l = v // 2
  r = M - l
  dp[l-1] += 1
  dp[r-1] += 1

# print(dp)

if len(set(dp)) == 1 and 2 in set(dp):
  print(2 ** (N // 2) % mod)
else:
  print(0)