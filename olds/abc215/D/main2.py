#!/usr/bin/env python3.8
import math

N, M = map(int, input().split())

*A, = map(int, input().split())

dp = {}

# count = 0
def gcd(a, k):
    if dp.get((a, k)):
        # global count
        # count += 1
        # print(count)
        return dp[(a, k)]
    if dp.get((k, a)):
        # global count
        # count += 1
        # print(count)
        return dp[(k, a)]


    if k == 1:
        dp[(a, k)] = k
        return 1

    r = a % k
    if r == 0:
        dp[(a, k)] = k
        return k

    o = gcd(k, r)
    dp[(a, k)] = o
    return o

ans = []
A.sort()

next_checks = list(range(1, M + 1))
for i, a in enumerate(A):
    if i % 10000 == 0:
        print(i)
    # print('a', a)
    checks = []
    for k in next_checks:
        if gcd(a, k) == 1:
            checks.append(k)
    # print('checks', checks)
    next_checks = checks

    if i == len(A) - 1:
        print('n', next_checks)
