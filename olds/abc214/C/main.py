#!/usr/bin/env python3.8
N = int(input())
*S, = map(int, input().split())
*T, = map(int, input().split())

dp = [9999999999999] * N

for i, t in enumerate(T):
    dp[i] = t

for i, s in enumerate(S):
    dp[(i + 1) % N] = min(dp[(i + 1) % N], dp[i] + S[i])

for i, s in enumerate(S):
    dp[(i + 1) % N] = min(dp[(i + 1) % N], dp[i] + S[i])

for d in dp:
    print(d)
