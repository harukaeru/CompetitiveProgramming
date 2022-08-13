#!/usr/bin/env python3
T = 'oxx'
S = input()

T = T * 10000

try:
  T.index(S)
  print('Yes')
except:
  print('No')