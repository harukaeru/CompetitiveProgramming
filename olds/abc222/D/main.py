#!/usr/bin/env python3.8
N = int(input())
*a, = map(int, input().split())
*b, = map(int, input().split())

MOD = 998244353  # type: int

M = 3000

# 場合の数
dp = [1] * (M + 1)

# for d in dp:
#     print(d)
#
# print('a', a)
# print('b', b)
for i in range(N):
    dx = [0] * (M + 1)
    for j in range(a[i], b[i] + 1):
        dx[j] = dp[j]

    for k in range(len(dx) - 1):
        dx[k + 1] = (dx[k] + dx[k + 1]) % MOD

    dp = dx
    # print(dp)

print(dp[M])
