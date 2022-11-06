#!/usr/bin/env python3.8
N = int(input())
x = hex(N).replace('0x', '').upper()
if len(x) == 1:
  print('0' + x)
else:
  print(x)