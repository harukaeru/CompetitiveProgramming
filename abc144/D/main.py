#!/usr/bin/env python3.8
from math import atan2, cos, degrees, pi, radians, sin, tan
import math

a,b,x=map(int, input().split())

s = x / a
if (a * a * b) / 2 <= x:
  t = a * b - s
  r = atan2(a, 2 * t / a)
else:
  r = atan2(2 * s / b, b)

print(90 - degrees(r))