#!/usr/bin/env python3
K = int(input())

s = ''
while K > 0:
  if K % 2:
    s = '2' + s
  else:
    s = '0' + s
  K //= 2

print(s)