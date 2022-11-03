#!/usr/bin/env python3
X, Y = input().split()

if X < Y:
  print('<')
elif X == Y:
  print('=')
else:
  print('>')