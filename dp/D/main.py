#!/usr/bin/env python3
N, W = map(int, input().split())

products = []
for i in range(N):
    w, v = map(int, input().split())
    products.append((w, v))

dp = [
    [0 for j in range(W + 1)]
    for i in range(N + 1)
]

for i in range(N):
    w, v = products[i]

    for j in range(W + 1):
        if j - w >= 0:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w] + v)
        else:
            dp[i + 1][j] = dp[i][j]

print(dp[N][W])
