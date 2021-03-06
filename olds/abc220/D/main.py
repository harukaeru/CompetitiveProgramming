#!/usr/bin/env python3

MOD = 998244353  # type: int

N = int(input())
*A, = map(int, input().split())

dp = [
    [0 for __ in range(10)]
    for __ in range(N)
]
dp[0][A[0]] = 1

for i, a in enumerate(A):  # range(len(A) - 1):
    if i == 0:
        continue
    d = dp[i - 1]
    dd = dp[i]
    for j in range(10):
        v = d[j]
        if v:
            aa = a % 10
            p = (j + aa)% 10
            q = (j * aa)% 10
            # print('p', p)
            # print('q', q)
            dd[p] += v % MOD
            dd[q] += v % MOD

for d in dp[N-1]:
    print(d % MOD)
