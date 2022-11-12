#!/usr/bin/env python3.8
N = int(input())
S = input()

x = 0
max_x = 0
for s in S:
  if s == 'I':
    x += 1
  else:
    x -= 1
  max_x = max(max_x, x)
print(max_x)
  
