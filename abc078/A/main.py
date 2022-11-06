#!/usr/bin/env python3.8
X, Y = input().split()

if X < Y:
  print('<')
elif X == Y:
  print('=')
else:
  print('>')