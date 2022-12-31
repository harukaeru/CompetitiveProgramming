#!/usr/bin/env python3.8
N, M = map(int, input().split())

t = (N - M) * 100
t += M * 1900

denom = 2 ** M
r = (denom - 1) / denom
a = 1 / denom
p = a / (1 - r)

ans = t * p / (1 - r)
print(int(ans))