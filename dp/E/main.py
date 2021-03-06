#!/usr/bin/env python3
N, W = map(int, input().split())

products = []
for i in range(N):
    w, v = map(int, input().split())
    products.append((w, v))

max_v = sum([p[1] for p in products])
INF = float('inf')
dp = [
    [INF for j in range(max_v + 1)]
    for i in range(N + 1)
]

dp[0][0] = 0

for i in range(N):
    w, v = products[i]

    # j以下の価値を満たせる最小の重さ(w)
    for j in range(max_v + 1):
        if j - v >= 0:
            dp[i + 1][j] = min(dp[i][j], dp[i][j - v] + w)
        else:
            dp[i + 1][j] = dp[i][j]

m = -1
for d in dp:
    for v, w in enumerate(d):
        if w <= W:
            m = max(m, v)
print(m)
