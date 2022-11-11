#!/usr/bin/env python3.8
W,a,b = map(int, input().split())

if b > (a+W):
  print(b - (a + W))
elif b + W < a:
  print(a - (b + W))
else:
  print(0)