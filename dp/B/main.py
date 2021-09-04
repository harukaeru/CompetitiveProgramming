#!/usr/bin/env python3
N, K = map(int, input().split())
*h, = map(int, input().split())

INF = 999999999

dp = [
    INF for i in range(N)
]

dp[0] = 0

for i in range(1, N):

    min_cost = INF
    max_back_point = max(0, i - K)
    for j in range(max_back_point, i):
        c = dp[j] + abs(h[j] - h[i])
        if min_cost > c:
            min_cost = c
    dp[i] = min_cost

print(dp[N-1])
