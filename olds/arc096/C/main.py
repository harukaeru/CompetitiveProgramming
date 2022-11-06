#!/usr/bin/env python3.8
A, B, C, X, Y = map(int, input().split())

maxXY = max(2 * X, 2 * Y)
m = 9999999999
for ab_count in range(maxXY + 1):
    a_count = X - (ab_count // 2)
    b_count = Y - (ab_count // 2)

    if a_count < 0:
        a_count = 0
    if b_count < 0:
        b_count = 0

    total_price = A * a_count + B * b_count + C * ab_count
    if m > total_price:
        m = total_price

print(m)
