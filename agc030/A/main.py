#!/usr/bin/env python3
A, B, C = map(int, input().split())

if A + B + 1 >= C:
  print(B + C)
else:
  print(B + (A + B + 1))