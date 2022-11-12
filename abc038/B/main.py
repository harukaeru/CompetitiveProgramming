#!/usr/bin/env python3.8
H1, W1 = map(int, input().split())
H2, W2 = map(int, input().split())

if H2 in [H1, W1] or W2 in [H1, W1]:
  print('YES')
else:
  print('NO')