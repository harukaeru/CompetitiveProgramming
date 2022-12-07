#!/usr/bin/env python3.8
x0, y0, x1, y1, x2, y2 = map(int, input().split())

x1 -= x0
y1 -= y0
x2 -= x0
y2 -= y0

print(abs((x1 * y2 - x2 * y1) / 2))