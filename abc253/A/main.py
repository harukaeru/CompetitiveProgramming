#!/usr/bin/env python3.8
x = list(map(int, input().split()))
b = x[1]
x.sort()
if x[1] == b:
  print('Yes')
else:
  print('No')