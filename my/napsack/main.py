N, W = map(int, input().split())

products = []
for i in range(N):
    w_i, v_i = map(int, input().split())
    products.append((w_i, v_i))

W = W  + 1
dp = [[0 for w in range(W)] for n in range(N + 1)]
from pprint import pprint

for i in range(N):
    p = products[i]
    p_w, p_v = p

    for w in range(W):
        if w - p_w >= 0:
            dp[i + 1][w] = max(dp[i][w], dp[i][w - p_w] + p_v)
        else:
            dp[i + 1][w] = dp[i][w]

    pprint(dp)
