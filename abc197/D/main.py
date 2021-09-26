#!/usr/bin/env python3
import math

N = int(input())
x_0, y_0 = map(int, input().split())
x_h, y_h = map(int, input().split())

x_m, y_m = (x_h + x_0) / 2, (y_h + y_0) / 2
d = x_0 - x_m, y_0 - y_m

r = math.atan2(d[1], d[0])
r = r + math.radians(360 / N)

dd = d[0] ** 2 + d[1] ** 2
d = math.sqrt(dd)

rotated_x = d * math.cos(r)
rotated_y = d * math.sin(r)

print(x_m + rotated_x, y_m + rotated_y)
