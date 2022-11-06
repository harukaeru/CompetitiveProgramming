#!/usr/bin/env python3.8
X = int(input())

A = [100, 101, 102, 103, 104, 105]

INF = 999999999999
dp = [INF] * (X + 1)
dp[0] = 0

for i in range(len(A)):
    a = A[i]
    for j in range(X + 1):
        if j - a >= 0:
            dp[j] = min(dp[j], dp[j - a] + a)

print(int(dp[X] != INF))
