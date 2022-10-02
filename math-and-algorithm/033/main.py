#!/usr/bin/env python3
import math
a_x, a_y = map(int, input().split())
b_x, b_y = map(int, input().split())
c_x, c_y = map(int, input().split())

ba = (a_x - b_x, a_y - b_y)
bc = (c_x - b_x, c_y - b_y)

ca = (a_x - c_x, a_y - c_y)
cb = (b_x - c_x, b_y - c_y)


if ba[0] * bc[0] + ba[1] * bc[1] < 0:
  print(math.sqrt(ba[0] ** 2 + ba[1] ** 2))
elif ca[0] * cb[0] + ca[1] * cb[1] < 0:
  print(math.sqrt(ca[0] ** 2 + ca[1] ** 2))
else:
  s = abs(ba[0] * bc[1] - ba[1] * bc[0])
  bottom = math.sqrt(bc[0] ** 2 + bc[1] ** 2)
  print(s / bottom)