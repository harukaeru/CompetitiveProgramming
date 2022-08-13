#!/usr/bin/env python3
x = list(map(int, input().split()))
b = x[1]
x.sort()
if x[1] == b:
  print('Yes')
else:
  print('No')