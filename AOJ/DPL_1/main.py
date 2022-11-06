#!/usr/bin/env python3.8

N, M = map(int, input().split())
*C, = map(int, input().split())

INF = 999999999
dp = [
    [INF for __ in range(N + 1)]
    for __ in range(M + 1)
]
for d in dp:
    d[0] = 0

for x in range(M):
    c = C[x]
    for y in range(N + 1):
        if y - c >= 0:
            dp[x + 1][y] = min(dp[x][y], dp[x + 1][y - c] + 1)
        else:
            dp[x + 1][y] = dp[x][y]

# for i, d in enumerate(dp):
#     print('i', i)
#     print('d[35]', d[35])
#     print('d[72]', d[72])
#     print('d[94]', d[94])
#     print('d[37]', d[37])
#     print('d[100]', d[100])
#     print('d', d)
print(dp[M][N])
