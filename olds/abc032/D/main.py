#!/usr/bin/env python3.8
N, W = map(int, input().split())

products = []
for i in range(N):
    v_i, w_i = map(int, input().split())
    products.append((v_i, w_i))

dp = [
    [0 for n in range(W + 1)]
    for n in range(N + 1)
]

for i in range(N):
    p = products[i]
    p_v, p_w = p

    for w in range(W + 1):
        dp[i + 1][w] = dp[i][w]
        if w - p_w >= 0:
            dp[i + 1][w] = max(dp[i][w], dp[i][w - p_w] + p_v)

print(dp[-1][W])
# from pprint import pprint
# pprint(dp)
