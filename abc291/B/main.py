#!/usr/bin/env python3.8
N = int(input())
X = list(map(int, input().split()))

X.sort()
s = X[N:4 * N]
print(sum(s) / (3 * N))