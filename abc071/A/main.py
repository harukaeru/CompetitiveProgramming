#!/usr/bin/env python3
x, a, b = map(int, input().split())

if abs(x - a) <= abs(x - b):
  print("A")
else:
  print("B")