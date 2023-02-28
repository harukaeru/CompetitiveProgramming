#!/usr/bin/env python3.8
from math import atan2, cos, pi, radians, sin, tan

a,b,x=map(int, input().split())

def calc(theta):
  theta = radians(theta)
  criteria = atan2(b, a)
  if theta >= criteria:
    return b * b * tan(pi / 2 - theta) * a / 2

  si = sin(theta)
  co = cos(theta)

  tot = (b ** 2) * si * co / 2 + a * b * co * co
  s = a * a * si * co / 2
  k = ((b * co - a * si) / (a * co)) ** 2 * s

  vv = tot - (s + k)
  return vv * a

l = 0
r = 90
# for i in range(90):
#   print(i, '->', calc(i))
while r - l >= 0.000000001:
  mid = (l + r) / 2
  v = calc(mid)
  # print(mid, '->', v)
  if v >= x:
    l = mid
  else:
    r = mid
# print(calc(45))
# print(l)
print((l + r) / 2)