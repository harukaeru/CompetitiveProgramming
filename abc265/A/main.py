#!/usr/bin/env python3.8
X, Y, N = map(int, input().split())

min_p = 99999999999
for i in range(100):
    for j in range(100):
        if i + 3 * j == N:
            min_p = min(min_p, i * X + j * Y)
print(min_p)
