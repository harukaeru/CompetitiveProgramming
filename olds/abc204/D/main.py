#!/usr/bin/env python3
N = int(input())
*T, = map(int, input().split())

MAX = sum(T)

T.sort()
T.reverse()

dp = [
    [False for __ in range(MAX + 1)]
    for _ in range(N + 1)
]

# m = MAX // 2 + 1

# dp[i][j] -> i個から何個か選んでjにできるか(true, false)
dp[0][0] = True

for i in range(N):
    t = T[i]
    for j in range(MAX + 1):
        if dp[i][j]:
            dp[i + 1][j] = True
        if j - t >= 0 and dp[i][j - t]:
            dp[i + 1][j] = True

m = 999999999999999999999
for d in dp:
    for j, v in enumerate(d):
        if v:
            maxj = max(j, MAX - j)
            m = min(m, maxj)


print(m)

