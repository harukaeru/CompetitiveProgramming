#!/usr/bin/env python3
import math
a,b,d = map(int, input().split())

d = math.radians(-d)
# print('d', d)
x = a * math.cos(d) + b * math.sin(d)
y = -a * math.sin(d) + b * math.cos(d)

print(x, y)