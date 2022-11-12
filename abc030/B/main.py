#!/usr/bin/env python3.8
import math
n, m = map(int, input().split())

n %= 12
n *= 30
n += 30 * m / 60
m = m * 6
# print(n, m)
print(min(abs(n - m), 360 - abs(n - m)))