#!/usr/bin/env python3.8
N, M = map(int, input().split())
a = []
for i in range(M):
  a.append(int(input()))

brokens = set(a)
MOD = 1000000007

dp = [0] * (N + 1)
dp[0] = 1
for i in range(N):
  if i + 1 <= N and i + 1 not in brokens:
    dp[i + 1] = (dp[i + 1] + dp[i]) % MOD
  if i + 2 <= N and i + 2 not in brokens:
    dp[i + 2] = (dp[i + 2] + dp[i]) % MOD

print(dp[N])
  