#!/usr/bin/env python3.8
x = list(map(int, input().split()))

if sum(x) - max(x) == max(x):
  print('Yes')
else:
  print('No')