#!/usr/bin/env python3.8
import math
x_1, y_1, r_1 = map(int, input().split())
x_2, y_2, r_2 = map(int, input().split())

if r_1 > r_2:
  tmp = x_2, y_2, r_2
  x_2, y_2, r_2 = x_1, y_1, r_1
  x_1, y_1, r_1 = tmp

d = math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)

if r_2 > d + r_1:
  print(1)
elif r_2 == d + r_1:
  print(2)
elif d - r_1 < r_2 < d + r_1:
  print(3)
elif d - r_1 == r_2:
  print(4)
else:
  print(5)