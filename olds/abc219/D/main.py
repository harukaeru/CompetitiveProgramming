#!/usr/bin/env python3
N = int(input())
X, Y = map(int, input().split())

pairs = []
for i in range(N):
    A, B = map(int, input().split())
    pairs.append((A, B))

INF = 9999999999999999
dp = [
    [
        [INF for k in range(Y + 1)]
        for j in range(X + 1)
    ]
    for i in range(N + 1)
]
dp[0][0][0] = 0

for i in range(N):
    a, b = pairs[i]
    # print('(a,b) = (', a, b, ')-------------------------')
    for j in range(X + 1):
        for k in range(Y + 1):
            origin_j = max(j - a, 0)
            origin_k = max(k - b, 0)
            dp[i + 1][j][k] = min(dp[i][j][k], dp[i][origin_j][origin_k] + 1)

# print(dp[N][W])

# for x, d in enumerate(dp):
#     print(x, '--------------------')
#     for dd in d:
#         print(dd)

ans = dp[N][X][Y]
if ans == INF:
    print(-1)
else:
    print(ans)
