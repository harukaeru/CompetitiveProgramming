#!/usr/bin/env python3
A, B = map(int, input().split())
if A + B >= 10:
  print('error')
else:
  print(A + B)