#!/usr/bin/env python3.8
X = int(input())

for a in range(-120, 121):
  for b in range(-120, 121):
    if a ** 5 - b ** 5 == X:
      print(a, b)
      exit()