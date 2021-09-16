#!/usr/bin/env python3
import math
R, X, Y = map(int, input().split())

d = math.sqrt(X * X + Y * Y)

# print(d, R)
# print(d // R)
r = 0
for i in range(int(d // R) + 1):
    r += R
    if d <= r:
        if d < r and i == 0:
            print(2)
        else:
            print(i + 1)
        exit()
