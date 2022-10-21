#!/usr/bin/env python3
N = int(input())

for i in range(1, 61):
  if N == 2 ** i - 1:
    print('Second')
    exit()
print('First')