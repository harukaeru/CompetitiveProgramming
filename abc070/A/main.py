#!/usr/bin/env python3.8
N = input()

if N == N[::-1]:
  print('Yes')
else:
  print('No')