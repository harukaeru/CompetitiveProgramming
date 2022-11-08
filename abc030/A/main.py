#!/usr/bin/env python3.8
A, B, C, D = map(int, input().split())

# A:B = C:D
if A * D < B * C:
  print('TAKAHASHI')
elif A * D == B * C:
  print('DRAW')
else:
  print('AOKI')